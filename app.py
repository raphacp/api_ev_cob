from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources import modalidade
from sql_alchemy import banco
from resources.atleta import Atletas, Atleta, AtletaCadastro
from resources.modalidade import Modalidades, Modalidade, ModalidadeCadastro
from resources.prova import Provas, Prova, ProvaCadastro
from resources.competicao import Competicoes, Competicao, CompeticaoCadastro
import sqlalchemy

username = 'root'
password = 'Cedes010'
host = 'localhost'
port = 3306
DB_NAME = 'app_ev_cob1'

# Inicializando o App
app = Flask(__name__)
# Se for usar outro banco é só mudar aqui
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://raphacp:Cedes010@raphacp.mysql.pythonanywhere-services.com/raphacp$app_ev_cob' # Banco Mysql no pythonanywhere
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Cedes010@127.0.0.1:3306/app_ev_cob1' # Banco local
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{username}:{password}@{host}:{port}/{DB_NAME}" # Banco local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#banco.init_app(app)
api = Api(app)
jwt = JWTManager(app)

# Exibindo uma mensagem na raiz do site
@app.route('/')
def index():
    return '<h1>API COB</h1><h2>Bem vindo.</h2>'

# Criacao do banco
@app.before_first_request # decorador
def cria_banco():
    # engine = sqlalchemy.create_engine('mysql://root:Cedes010@127.0.0.1:3306/app_ev_cob1') # Conectando ao banco
    engine = sqlalchemy.create_engine(f"mysql://{username}:{password}@{host}:{port}") # Conectando ao banco
    # engine.execute("CREATE DATABASE IF NOT EXISTS app_ev_cob1") # Criando o banco
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}") # Criando o banco
    engine.execute(f"USE {DB_NAME}") # Setando o banco
    banco.create_all()

# Criando os endpoints
api.add_resource(Atletas, '/atletas')
api.add_resource(Atleta, '/atletas/<string:id>')
api.add_resource(AtletaCadastro, '/atletas/cadastro')
api.add_resource(Modalidades, '/modalidades')
api.add_resource(Modalidade, '/modalidades/<string:id>')
api.add_resource(ModalidadeCadastro, '/modalidades/cadastro')
api.add_resource(Provas, '/provas')
api.add_resource(Prova, '/provas/<string:id>')
api.add_resource(ProvaCadastro, '/provas/cadastro')
api.add_resource(Competicoes, '/competicoes')
api.add_resource(Competicao, '/competicoes/<string:id>')
api.add_resource(CompeticaoCadastro, '/competicoes/cadastro')

if __name__ == '__main__':
    banco.init_app(app)
    app.run(debug=True)
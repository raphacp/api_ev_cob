from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from sql_alchemy import banco
from resources.atleta import Atletas, Atleta, AtletaCadastro

# Inicializando o App
app = Flask(__name__)
# Se for usar outro banco é só mudar aqui
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://raphacp:Cedes010@raphacp.mysql.pythonanywhere-services.com/raphacp$app_ev_cob' # Banco Mysql no pythonanywhere
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Cedes010@127.0.0.1:3306/app_ev_cob' # Banco local
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
    banco.create_all()

# Criando os endpoints
api.add_resource(Atletas, '/atletas')
api.add_resource(Atleta, '/atleta/<string:id>')
api.add_resource(AtletaCadastro, '/atleta/cadastro')

if __name__ == '__main__':
    banco.init_app(app)
    app.run(debug=True)
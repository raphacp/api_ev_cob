from flask import Flask
from flask_restful import Api
from sql_alchemy import banco
from resources.atleta import Atletas, Atleta, AtletaCadastro
from resources.modalidade import Modalidades, Modalidade, ModalidadeCadastro
from resources.prova import Provas, Prova, ProvaCadastro
from resources.competicao import Competicoes, Competicao, CompeticaoCadastro
from resources.competicao_atleta import CompeticoesAtletas, CompeticaoAtleta, Competicao_AtletaCadastro
from resources.atleta_prova import AtletasProvas, AtletaProva, AtletaProvaCadastro
from resources.consulta_resultado import Consulta_Resultados
from resources.consulta_atleta import Consulta_Atletas
from resources.consulta_ranking import Consulta_Ranking
import sqlalchemy

# Dados do banco de dados.
# Rever na refatoracao
username = 'root'
password = 'Cedes010'
host = 'localhost'
port = 3306
DB_NAME = 'api_ev_cob'

# Inicializando o App
app = Flask(__name__)
# Se for usar outro banco é só mudar aqui
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://raphacp:Cedes010@raphacp.mysql.pythonanywhere-services.com/raphacp$app_ev_cob' # Banco Mysql no pythonanywhere
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Cedes010@127.0.0.1:3306/app_ev_cob1' # Banco local
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{username}:{password}@{host}:{port}/{DB_NAME}" # Banco local parametrizado
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#banco.init_app(app) # Usado aqui qd executado no pythonanywhere
api = Api(app)

# Exibindo uma mensagem na raiz do site
@app.route('/')
def index():
    return '<h1>API COB</h1><h2>Bem vindo.</h2>'

# Criacao do banco
@app.before_first_request # decorador
def cria_banco():
    engine = sqlalchemy.create_engine(f"mysql://{username}:{password}@{host}:{port}") # Conectando ao banco
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}") # Criando o banco
    engine.execute(f"USE {DB_NAME}") # Setando o banco
    banco.create_all()
    engine.execute("CREATE OR REPLACE VIEW competicao_prova_atleta AS \
                    SELECT c.evento, c.id_prova, p.nome as prova, p.unidade_medida, c.id as id_competicao, c.nome as competicao, \
                    c.sexo, c.paralimpico, c.tipo_bateria as bateria, c.data_inicio, c.data_final, a.id as id_atleta, a.nome as atleta, \
                    a.pais, ca.resultado_1, ca.resultado_2, ca.resultado_3, GREATEST(IFNULL(resultado_1, 0), IFNULL(resultado_2, 0), \
                    IFNULL(resultado_3, 0)) as maior_resultado \
                    FROM competicao c, prova p, competicao_atleta ca, atleta a \
                    WHERE c.id_prova = p.id and ca.id_competicao = c.id and ca.id_atleta = a.id;") # Criando uma view com os dados da competição, prova e atleta
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
api.add_resource(CompeticoesAtletas, '/competicoes_atletas')
api.add_resource(CompeticaoAtleta, '/competicoes_atletas/<string:id>')
api.add_resource(Competicao_AtletaCadastro, '/competicoes_atletas/cadastro')
api.add_resource(AtletasProvas, '/atletas_provas')
api.add_resource(AtletaProva, '/atletas_provas/<string:id>')
api.add_resource(AtletaProvaCadastro, '/atletas_provas/cadastro')
api.add_resource(Consulta_Resultados, '/consultas/resultados')
api.add_resource(Consulta_Atletas, '/consultas/atletas')
api.add_resource(Consulta_Ranking, '/consultas/ranking')

if __name__ == '__main__':
    banco.init_app(app)
    app.run(debug=True)
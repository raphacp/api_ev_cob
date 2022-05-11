from sql_alchemy import banco
from sqlalchemy_utils import create_view
from sqlalchemy import create_engine, MetaData


username = 'root'
password = 'Cedes010'
host = 'localhost'
port = 3306
DB_NAME = 'api_ev_cob'

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}") # Conectando ao banco
engine.execute(f"USE {DB_NAME}") # Setando o banco
view = engine.execute("CREATE OR REPLACE VIEW competicao_prova_atleta AS \
                    SELECT c.evento, c.id_prova, p.nome as prova, p.unidade_medida, c.id as id_competicao, c.nome as competicao, \
                    c.sexo, c.paralimpico, c.tipo_bateria as bateria, c.data_inicio, c.data_final, a.id as id_atleta, a.nome as atleta,\
                    a.pais, ca.resultado_1, ca.resultado_2, ca.resultado_3, GREATEST(IFNULL(resultado_1, 0), IFNULL(resultado_2, 0), \
                    IFNULL(resultado_3, 0)) as maior_resultado \
                    FROM competicao c, prova p, competicao_atleta ca, atleta a \
                    WHERE c.id_prova = p.id and ca.id_competicao = c.id and ca.id_atleta = a.id") # Criando uma view com os dados da competição, prova e atleta
banco.create_all()

# Criacao da tabela atleta_prova no banco de dados

class RankinkViewModel(banco):

    __table__ = view
    
    def __init__(self, evento, id_prova, prova, unidade_medida, id_competicao, competicao, sexo, paralimpico, bateria, data_inicio, 
    data_final, id_atleta, atleta, pais, resultado_1, resultado_2, resultado_3, maior_resultado):

        self.evento = evento
        self.id_prova = id_prova        
        self.prova = prova
        self.unidade_medida = unidade_medida
        self.id_competicao = id_competicao
        self.competicao = competicao
        self.sexo = sexo
        self.paralimpico = paralimpico
        self.bateria = bateria
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.id_atleta = id_atleta
        self.atleta = atleta
        self.pais = pais
        self.resultado_1 = resultado_1
        self.resultado_2 = resultado_2
        self.resultado_3 = resultado_3
        self.maior_resultado = maior_resultado

    def json(self):
        return{
            'evento': self.evento,
            'id_prova': self.id_prova,
            'prova': self.prova,
            'unidade_medida': self.unidade_medida,
            'id_competicao': self.id_competicao,
            'competicao': self.competicao,
            'sexo': self.sexo,
            'paralimpico': self.paralimpico,
            'bateria': self.bateria,
            'data_inicio': self.data_inicio,
            'data_final': self.data_final,
            'id_atleta': self.id_atleta,
            'atleta': self.atleta,
            'pais': self.pais,
            'resultado_1': self.resultado_1,
            'resultado_2': self.resultado_2,
            'resultado_3': self.resultado_3,
            'maior_resultado': self.maior_resultado
        }

    # @classmethod # Decorador
    # def find_atleta_prova(cls, id):
    #     atleta_prova = cls.query.filter_by(id=id).first() # SELECT * FROM atleta_prova WHERE id = id LIMIT 1
    #     if atleta_prova: # = if atleta_prova is not null
    #         return atleta_prova
    #     return None

    # @classmethod
    # def find_by_atleta_prova(cls, id_atleta, id_prova):
    #     # SELECT * FROM atleta_prova WHERE id_atleta = id_atleta and id_prova = id_prova LIMIT 1
    #     atleta_prova = cls.query.filter(cls.id_atleta==id_atleta, cls.id_prova==id_prova).first() 
    #     if atleta_prova: # = if atleta_prova is not null
    #         return atleta_prova
    #     return None

    # def save_atleta_prova(self):
    #     banco.session.add(self)
    #     banco.session.commit()

    # def update_atleta_prova(self, id_atleta, id_prova):
    #     self.id_atleta = id_atleta
    #     self.id_prova = id_prova
        

    # def delete_atleta_prova(self):
    #     banco.session.delete(self)
    #     banco.session.commit()

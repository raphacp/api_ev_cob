from asyncio.windows_events import NULL
from sql_alchemy import banco
from models.competicao import CompeticaoModel

# Criacao da tabela modalidade no banco de dados
class CompeticaoAtletaModel(banco.Model):
    __tablename__ = 'competicao_atleta'
    # __table_args__ = PrimaryKeyConstraint('id_competicao', 'id_atleta')

    id = banco.Column(banco.Integer, primary_key=True)
    id_competicao = banco.Column(banco.Integer, banco.ForeignKey('competicao.id'))
    id_atleta = banco.Column(banco.Integer, banco.ForeignKey('atleta.id'))
    resultado_1 = banco.Column(banco.Float)
    resultado_2 = banco.Column(banco.Float)
    resultado_3 = banco.Column(banco.Float)
    constraint_competicao_atleta = banco.UniqueConstraint(id_competicao, id_atleta, name='competicao_atleta')

    def __init__(self, id_competicao, id_atleta, resultado_1, resultado_2, resultado_3): # Não coloca o id aqui pq ele sera criado automaticamente (auto_increment)
        self.id_competicao = id_competicao
        self.id_atleta = id_atleta
        self.resultado_1 = resultado_1
        self.resultado_2 = resultado_2
        self.resultado_3 = resultado_3

    def json(self):
        return{
            'id': self.id,
            'id_competicao': self.id_competicao,
            'id_atleta': self.id_atleta,
            'resultado_1': self.resultado_1,
            'resultado_2': self.resultado_2,
            'resultado_3': self.resultado_3,
        }

    @classmethod # Decorador
    def find_competicao_atleta(cls, id):
        competicao_atleta = cls.query.filter_by(id=id).first() # SELECT * FROM competicao_atleta WHERE id = id LIMIT 1
        if competicao_atleta: # = if competicao_atleta is not null
            return competicao_atleta
        return None

    @classmethod
    def find_by_competicao_atleta(cls, id_competicao, id_atleta):
        # SELECT * FROM competicao_atleta WHERE id_competicao = id_competicao and id_atleta = id_atleta LIMIT 1
        competicao_atleta = cls.query.filter(cls.id_competicao==id_competicao, cls.id_atleta==id_atleta).first() 
        if competicao_atleta: # = if competicao_atleta is not null
            return competicao_atleta
        return None
        
    @classmethod
    def find_competicao_atleta_encerrada(cls, id_competicao):
        # SELECT * FROM competicao_atleta, competicao WHERE id_competicao = competicao.id and competicao.data_final != null LIMIT 1
        competicao_encerrada = cls.query.filter(id_competicao == CompeticaoModel.id, CompeticaoModel.data_final != NULL).first()
        # return {'message': 'Resultado: {}'.format(competicao_encerrada)}
        if competicao_encerrada: # = if competicao_encerrada is not null
            return competicao_encerrada
        return None

    def save_competicao_atleta(self):
        banco.session.add(self)
        banco.session.commit()

    def update_competicao_atleta(self, id_competicao, id_atleta, resultado_1, resultado_2, resultado_3):
        self.id_competicao = id_competicao
        self.id_atleta = id_atleta
        self.resultado_1 = resultado_1
        self.resultado_2 = resultado_2
        self.resultado_3 = resultado_3

    def delete_competicao_atleta(self):
        banco.session.delete(self)
        banco.session.commit()

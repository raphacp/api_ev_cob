from sqlalchemy import PrimaryKeyConstraint
from sql_alchemy import banco

# Criacao da tabela modalidade no banco de dados
class CompeticaoAtletaModel(banco.Model):
    __tablename__ = 'competicao_atleta'
    # __table_args__ = PrimaryKeyConstraint('id_competicao', 'id_atleta')

    id_competicao = banco.Column(banco.Integer, banco.ForeignKey('competicao.id'), primary_key=True)
    id_atleta = banco.Column(banco.Integer, banco.ForeignKey('atleta.id'), primary_key=True)
    resultado_1 = banco.Column(banco.Float)
    resultado_2 = banco.Column(banco.Float)
    resultado_3 = banco.Column(banco.Float)
    # id_competicao = banco.Column(banco.Integer, banco.ForeignKey('competicao.id')) #inserindo chave estrangeira
    # id_atleta = banco.Column(banco.Integer, banco.ForeignKey('atleta.id')) #inserindo chave estrangeira

    def __init__(self, id_competicao, id_atleta, resultado_1, resultado_2, resultado_3):
        self.id_competicao = id_competicao
        self.id_atleta = id_atleta
        self.resultado_1 = resultado_1
        self.resultado_2 = resultado_2
        self.resultado_3 = resultado_3

    def json(self):
        return{
            'id_competicao': self.id_competicao,
            'id_atleta': self.id_atleta,
            'resultado_1': self.resultado_1,
            'resultado_2': self.resultado_2,
            'resultado_3': self.resultado_3,
        }

    @classmethod # Decorador
    def find_competicao_atleta(cls, id_competicao, id_atleta):
        competicao_atleta = cls.query.filter_by(id_competicao==id_competicao and id_atleta==id_atleta).first() # SELECT * FROM competicao_atleta WHERE id = id LIMIT 1
        if competicao_atleta: # = if competicao_atleta is not null
            return competicao_atleta
        return None

    # @classmethod
    # def find_by_name(cls, nome):
    #     competicao_atleta = cls.query.filter_by(nome=nome).first() # SELECT * FROM competicao_atleta WHERE nome = nome LIMIT 1
    #     if competicao_atleta: # = if competicao_atleta is not null
    #         return competicao_atleta
    #     return None

    # def save_competicao_atleta(self):
    #     banco.session.add(self)
    #     banco.session.commit()

    # def update_competicao_atleta(self, resultado_1, resultado_2, resultado_3):
    #     self.resultado_1 = resultado_1
    #     self.resultado_2 = resultado_2
    #     self.resultado_3 = resultado_3

    # def delete_competicao_atleta(self):
    #     # ************ Verificar se sera necessario ****************
    #     # Deletando todas as provas associadas a competicao_atleta
    #     # [prova.delete_prova() for prova in self.provas]
    #     # Deletando a competicao_atleta
    #     banco.session.delete(self)
    #     banco.session.commit()

from email.policy import default
from sql_alchemy import banco
import json
import datetime

# Criacao da tabela competicao no banco de dados
class CompeticaoModel(banco.Model):
    __tablename__ = 'competicao'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(150), nullable=False)
    #data_inicio = banco.Column(banco.DateTime, nullable=False)
    data_inicio = banco.Column(banco.DateTime)    
    data_final = banco.Column(banco.DateTime)
    sexo = banco.Column(banco.Enum("Masculino", "Feminino"))
    paralimpico = banco.Column(banco.Enum("Sim", "Nao"))
    id_prova = banco.Column(banco.Integer, banco.ForeignKey('prova.id')) #inserindo chave estrangeira

    def __init__(self, nome, data_inicio, data_final, sexo, paralimpico, id_prova):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.sexo = sexo
        self.paralimpico = paralimpico
        self.id_prova = id_prova

    # @classmethod
    def converte_datetime_str(campo):
        if isinstance(campo, datetime.datetime):
            return campo.isoformat()
            # return campo.__str__()

    def json(self):
        # saida = {
        #     'id': self.id,
        #     'nome': self.nome,
        #     'data_inicio': self.data_inicio,
        #     'data_final': self.data_final,
        #     'sexo': self.sexo,
        #     'paralimpico': self.paralimpico,
        #     'id_prova': self.id_prova
        #     }

        # saida_formatada_data = json.dumps(saida, default=str)
        # return saida_formatada_data
        # if isinstance(self.data_inicio, datetime.datetime):
        #     return {'message': 'Data inicio é datetime'}
        # 'data_final': json.dumps(self.data_final, default=CompeticaoModel.converte_datetime_str()),

        return{
            'id': self.id,
            'nome': self.nome,
            'data_inicio': json.dumps(self.data_inicio, default=CompeticaoModel.converte_datetime_str),
            'data_final': json.dumps(self.data_final, default=CompeticaoModel.converte_datetime_str),
            'sexo': self.sexo,
            'paralimpico': self.paralimpico,
            'id_prova': self.id_prova
            }

    @classmethod # Decorador
    def find_competicao(cls, id):
        competicao = cls.query.filter_by(id=id).first() # SELECT * FROM competicao WHERE id = id LIMIT 1
        if competicao: # = if competicao is not null
            return competicao
        return None

    @classmethod
    def find_by_name(cls, nome):
        competicao = cls.query.filter_by(nome=nome).first() # SELECT * FROM competicao WHERE nome = nome LIMIT 1
        if competicao: # = if competicao is not null
            return competicao
        return None

    def save_competicao(self):
        banco.session.add(self)
        banco.session.commit()

    def update_competicao(self, nome, data_inicio, data_final, sexo, paralimpico, id_prova):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.sexo = sexo
        self.paralimpico = paralimpico
        self.id_prova = id_prova

    def delete_competicao(self):
        banco.session.delete(self)
        banco.session.commit()

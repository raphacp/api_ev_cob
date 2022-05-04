from sql_alchemy import banco
from models.competicao_atleta import CompeticaoAtletaModel

# Criacao da tabela atleta no banco de dados
class AtletaModel(banco.Model):
    __tablename__ = 'atleta'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(150), nullable=False)
    pais = banco.Column(banco.String(100), nullable=False)
    sexo = banco.Column(banco.Enum("Masculino", "Feminino"))
    paralimpico = banco.Column(banco.Enum("Sim", "Nao"))
    competicoes_atletas = banco.relationship('CompeticaoAtletaModel') # Criando o relacionamento entre tabelas/classes. Lista de objetos competicao_atletas

    def __init__(self, nome, pais, sexo, paralimpico): #não coloca o id aqui pq ele sera criado automaticamente (auto_increment)
        self.nome = nome
        self.pais = pais
        self.sexo = sexo
        self.paralimpico = paralimpico

    def json(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'pais': self.pais,
            'sexo': self.sexo,
            'paralimpico': self.paralimpico,
            'competicoes': [competicoes_atletas.json() for competicoes_atletas in self.competicoes_atletas]
        }

    @classmethod # Decorador
    def find_atleta(cls, id):
        atleta = cls.query.filter_by(id=id).first() # SELECT * FROM atleta WHERE id = id LIMIT 1
        if atleta: # = if atleta is not null
            return atleta
        return None

    @classmethod
    def find_by_name(cls, nome):
        atleta = cls.query.filter_by(nome=nome).first() # SELECT * FROM atleta WHERE nome = nome LIMIT 1
        if atleta: # = if atleta is not null
            return atleta
        return None

    def save_atleta(self):
        banco.session.add(self)
        banco.session.commit()

    def update_atleta(self, nome, pais, sexo, paralimpico):
        self.nome = nome
        self.pais = pais
        self.sexo = sexo
        self.paralimpico = paralimpico

    def delete_atleta(self):
        banco.session.delete(self)
        banco.session.commit()

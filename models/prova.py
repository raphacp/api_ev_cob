from sql_alchemy import banco

# Criacao da tabela prova no banco de dados
class ProvaModel(banco.Model):
    __tablename__ = 'prova'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(150), nullable=False)
    unidade_medida = banco.Column(banco.Enum("s", "m"))
    id_modalidade = banco.Column(banco.Integer, banco.ForeignKey('modalidade.id')) #inserindo chave estrangeira

    def __init__(self, nome, unidade_medida, id_modalidade):
        self.nome = nome
        self.unidade_medida = unidade_medida
        self.id_modalidade = id_modalidade

    def json(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'unidade_medida': self.unidade_medida,
            'id_modalidade': self.id_modalidade
            }

    @classmethod # Decorador
    def find_prova(cls, id):
        prova = cls.query.filter_by(id=id).first() # SELECT * FROM prova WHERE id = id LIMIT 1
        if prova: # = if prova is not null
            return prova
        return None

    @classmethod
    def find_by_name(cls, nome):
        prova = cls.query.filter_by(nome=nome).first() # SELECT * FROM prova WHERE nome = nome LIMIT 1
        if prova: # = if prova is not null
            return prova
        return None

    def save_prova(self):
        banco.session.add(self)
        banco.session.commit()

    def update_prova(self, nome, unidade_medida, id_modalidade):
        self.nome = nome
        self.unidade_medida = unidade_medida
        self.id_modalidade = id_modalidade

    def delete_prova(self):
        banco.session.delete(self)
        banco.session.commit()

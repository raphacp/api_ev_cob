from sql_alchemy import banco

# Criacao da tabela modalidade no banco de dados
class ModalidadeModel(banco.Model):
    __tablename__ = 'modalidade'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(150), nullable=False)
    provas = banco.relationship('ProvaModel') # Criando o relacionamento entre tabelas/classes. Lista de objetos prova

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'provas': [prova.json() for prova in self.provas]
        }

    @classmethod # Decorador
    def find_modalidade(cls, id):
        modalidade = cls.query.filter_by(id=id).first() # SELECT * FROM modalidade WHERE id = id LIMIT 1
        if modalidade: # = if modalidade is not null
            return modalidade
        return None

    @classmethod
    def find_by_name(cls, nome):
        modalidade = cls.query.filter_by(nome=nome).first() # SELECT * FROM modalidade WHERE nome = nome LIMIT 1
        if modalidade: # = if modalidade is not null
            return modalidade
        return None

    def save_modalidade(self):
        banco.session.add(self)
        banco.session.commit()

    def update_modalidade(self, nome):
        self.nome = nome

    def delete_modalidade(self):
        # ************ Verificar se será necessário ****************
        # Deletando todos os hoteis associados ao site
        # [prova.delete_hotel() for prova in self.provas]
        # Deletando a modalidade
        banco.session.delete(self)
        banco.session.commit()

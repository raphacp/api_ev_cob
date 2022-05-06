from sql_alchemy import banco

# Criacao da tabela atleta_prova no banco de dados
class AtletaProvaModel(banco.Model):
    __tablename__ = 'atleta_prova'

    id = banco.Column(banco.Integer, primary_key=True)
    id_atleta = banco.Column(banco.Integer, banco.ForeignKey('atleta.id'))
    id_prova = banco.Column(banco.Integer, banco.ForeignKey('prova.id'))
    constraint_atleta_prova = banco.UniqueConstraint( id_atleta, id_prova, name='atleta_prova')
    
    def __init__(self, id_atleta, id_prova):
        self.id_atleta = id_atleta
        self.id_prova = id_prova

    def json(self):
        return{
            'id': self.id,
            'id_atleta': self.id_atleta,
            'id_prova': self.id_prova
        }

    @classmethod # Decorador
    def find_atleta_prova(cls, id):
        atleta_prova = cls.query.filter_by(id=id).first() # SELECT * FROM atleta_prova WHERE id = id LIMIT 1
        if atleta_prova: # = if atleta_prova is not null
            return atleta_prova
        return None

    @classmethod
    def find_by_atleta_prova(cls, id_atleta, id_prova):
        # SELECT * FROM atleta_prova WHERE id_atleta = id_atleta and id_prova = id_prova LIMIT 1
        atleta_prova = cls.query.filter(cls.id_atleta==id_atleta, cls.id_prova==id_prova).first() 
        if atleta_prova: # = if atleta_prova is not null
            return atleta_prova
        return None

    def save_atleta_prova(self):
        banco.session.add(self)
        banco.session.commit()

    def update_atleta_prova(self, id_atleta, id_prova):
        self.id_atleta = id_atleta
        self.id_prova = id_prova
        

    def delete_atleta_prova(self):
        banco.session.delete(self)
        banco.session.commit()

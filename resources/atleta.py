from flask_restful import Resource, reqparse
from models.atleta import AtletaModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="O campo Nome não pode ser vazio.")
atributos.add_argument('pais', type=str, required=True, help="O campo País não pode ser vazio.")
atributos.add_argument('sexo', type=str, required=True, help="O campo sexo não pode ser vazio.")
atributos.add_argument('paralimpico', type=str, required=True, help="O campo Paralimpico não pode ser vazio.")

class Atletas(Resource):
    # /atletas
    def get(self):
        return {'atletas': [atleta.json() for atleta in AtletaModel.query.all()]}

class Atleta(Resource):
    # /atleta/{id}
    def get(self, id):
        atleta = AtletaModel.find_atleta(id)
        if atleta: # = if atleta is not null
            return atleta.json()
        return {"message": "Atleta '{}' não encontrado.".format(id)}, 404 #status code not found
    

    def put(self, id):
        dados = atributos.parse_args()
        atleta_encontrado = AtletaModel.find_atleta(id)
        if atleta_encontrado:
            atleta_encontrado.update_atleta(**dados)
            atleta_encontrado.save_atleta()
            return atleta_encontrado.json(), 200 # OK
        atleta = AtletaModel(id, **dados) # Cria a instancia do atleta
        try:
            atleta.save_atleta()
        except:
            return {"message": "Ocorreu um erro intero ao salvar os dados do atleta '{}'.".format(id)}, 500 # Internal Server Error}
        return atleta.json(), 201 # created


    def delete(self, id):
        atleta = AtletaModel.find_atleta(id)
        if atleta:
            try: 
                atleta.delete_atleta()
            except:
                return {"message": "Ocorreu um erro intero ao tentar deletar os dados do atleta '{}'.".format(id)}, 500 # Internal Server Error}
            return {"message": "Atleta '{}' deletado.".format(id)}, 200 # OK
        return {"message": "Atleta '{}' não encontrado.".format(id)}, 404


class AtletaCadastro(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()
        if AtletaModel.find_by_name(dados['nome']):
            return {"message": "O atleta '{}' já existe.".format(dados['nome'])}, 400 # bad request       
        atleta = AtletaModel(**dados) # Instanciando o obsjeto
        try:
            atleta.save_atleta()
            #return {"message": "Atleta '{}'criado com sucesso!".format(dados['nome'])}, 200 # Criado
        except:
            return {"message": "Ocorreu um erro intero ao cadastrar o atleta '{}'.".format(dados['nome'])}, 500
        return atleta.json(), 201 # created


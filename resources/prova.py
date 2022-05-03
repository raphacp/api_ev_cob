from flask_restful import Resource, reqparse
from models.prova import ProvaModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="O campo Nome não pode ser vazio.")
atributos.add_argument('unidade_medida', type=str, required=True, help="O campo unidade_medida não pode ser vazio.")
atributos.add_argument('id_modalidade', type=int, required=True, help="Toda prova precisa estar linkada com uma modalidade.")

class Provas(Resource):
    # /provas
    def get(self):
        return {'provas': [prova.json() for prova in ProvaModel.query.all()]}

class Prova(Resource):
    # /provas/{id}
    def get(self, id):
        prova = ProvaModel.find_prova(id)
        if prova: # = if prova is not null
            return prova.json()
        return {"message": "Prova '{}' não encontrada.".format(id)}, 404 #status code not found
    

    def put(self, id):
        dados = atributos.parse_args()
        prova_encontrada = ProvaModel.find_prova(id)
        if prova_encontrada:
            prova_encontrada.update_prova(**dados)
            prova_encontrada.save_prova()
            return prova_encontrada.json(), 200 # OK
        prova = ProvaModel(id, **dados) # Cria a instancia prova
        try:
            prova.save_prova()
        except:
            return {"message": "Ocorreu um erro intero ao salvar os dados da prova '{}'.".format(id)}, 500 # Internal Server Error}
        return prova.json(), 201 # created


    def delete(self, id):
        prova = ProvaModel.find_prova(id)
        if prova:
            try: 
                prova.delete_prova()
            except:
                return {"message": "Ocorreu um erro intero ao tentar deletar os dados da prova '{}'.".format(id)}, 500 # Internal Server Error}
            return {"message": "Prova '{}' deletada.".format(id)}, 200 # OK
        return {"message": "Prova '{}' não encontrada.".format(id)}, 404


class ProvaCadastro(Resource):
    # /provas/cadastro
    def post(self):
        dados = atributos.parse_args()
        if ProvaModel.find_by_name(dados['nome']):
            return {"message": "A prova '{}' já existe.".format(dados['nome'])}, 400 # bad request       
        prova = ProvaModel(**dados) # Instanciando o objeto
        try:
            prova.save_prova()
        except:
            return {"message": "Ocorreu um erro interno ao cadastrar a prova '{}'.".format(dados['nome'])}, 500
        return prova.json(), 201 # created


from flask_restful import Resource, reqparse
from models.modalidade import ModalidadeModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="O campo Nome não pode ser vazio.")

class Modalidades(Resource):
    # /modalidades
    def get(self):
        return {'modalidades': [modalidade.json() for modalidade in ModalidadeModel.query.all()]}

class Modalidade(Resource):
    # /modalidade/{id}
    def get(self, id):
        modalidade = ModalidadeModel.find_modalidade(id)
        if modalidade: # = if modalidade is not null
            return modalidade.json()
        return {"message": "Modalidade '{}' não encontrada.".format(id)}, 404 #status code not found
    

    def put(self, id):
        dados = atributos.parse_args()
        modalidade_encontrada = ModalidadeModel.find_modalidade(id)
        if modalidade_encontrada:
            modalidade_encontrada.update_modalidade(**dados)
            modalidade_encontrada.save_modalidade()
            return modalidade_encontrada.json(), 200 # OK
        modalidade = ModalidadeModel(id, **dados) # Cria a instancia modalidade
        try:
            modalidade.save_modalidade()
        except:
            return {"message": "Ocorreu um erro intero ao salvar os dados de modalidade '{}'.".format(id)}, 500 # Internal Server Error}
        return modalidade.json(), 201 # created


    def delete(self, id):
        modalidade = ModalidadeModel.find_modalidade(id)
        if modalidade:
            try: 
                modalidade.delete_modalidade()
            except:
                return {"message": "Ocorreu um erro intero ao tentar deletar os dados de modalidade '{}'.".format(id)}, 500 # Internal Server Error}
            return {"message": "Modalidade '{}' deletada.".format(id)}, 200 # OK
        return {"message": "Modalidade '{}' não encontrada.".format(id)}, 404


class ModalidadeCadastro(Resource):
    # /modalidade/cadastro
    def post(self):
        dados = atributos.parse_args()
        if ModalidadeModel.find_by_name(dados['nome']):
            return {"message": "A modalidade '{}' já existe.".format(dados['nome'])}, 400 # bad request       
        modalidade = ModalidadeModel(**dados) # Instanciando o objeto
        try:
            modalidade.save_modalidade()
        except:
            return {"message": "Ocorreu um erro intero ao cadastrar a modalidade '{}'.".format(dados['nome'])}, 500
        return modalidade.json(), 201 # created


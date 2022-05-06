from flask_restful import Resource, reqparse
from models.atleta_prova import AtletaProvaModel

atributos = reqparse.RequestParser()
atributos.add_argument('id_atleta', type=str, required=True, help="O campo id_atleta não pode ser vazio.")
atributos.add_argument('id_prova', type=str, required=True, help="O campo id_prova não pode ser vazio.")


class AtletasProvas(Resource):
    # /atletas_provas
    def get(self):
        return {'atletas_provas': [competicao.json() for competicao in AtletaProvaModel.query.all()]}

class AtletaProva(Resource):
    # /atletas_provas/{id}
    def get(self, id):
        atleta_prova = AtletaProvaModel.find_atleta_prova(id)
        if atleta_prova: # = if atleta_prova is not null
            return atleta_prova.json()
        return {"message": "Associação Atleta-Prova '{}' não encontrada.".format(id)}, 404 #status code not found
    

    def put(self, id):
        dados = atributos.parse_args()
        atleta_prova_encontrada = AtletaProvaModel.find_atleta_prova(id)
        if atleta_prova_encontrada:          
            atleta_prova_encontrada.update_atleta_prova(**dados)
            atleta_prova_encontrada.save_atleta_prova()
            return atleta_prova_encontrada.json(), 200 # OK
        atleta_prova = AtletaProvaModel(id, **dados) # Cria a instancia atleta_prova
        try:
            atleta_prova.save_atleta_prova()
        except:
            return {"message": "Ocorreu um erro interno ao salvar os dados de atleta_prova '{}'.".format(id)}, 500 # Internal Server Error}
        return atleta_prova.json(), 201 # created


    def delete(self, id):
        atleta_prova = AtletaProvaModel.find_atleta_prova(id)
        if atleta_prova:
            try: 
                atleta_prova.delete_atleta_prova()
            except:
                return {"message": "Ocorreu um erro intero ao tentar deletar os dados de atleta_prova '{}'.".format(id)}, 500 # Internal Server Error}
            return {"message": "Associação Atleta-Prova '{}' deletada.".format(id)}, 200 # OK
        return {"message": "Associação Atleta-Prova '{}' não encontrada.".format(id)}, 404


class AtletaProvaCadastro(Resource):
    # # /atletas_provas/cadastro
    def post(self):
        dados = atributos.parse_args()
        if AtletaProvaModel.find_by_atleta_prova(dados['id_atleta'], dados['id_prova']):
            return {"message": "A associação atleta_prova '{} e {}' já existe.".format(dados['id_atleta'], dados['id_prova'])}, 400 # bad request       
        atleta_prova = AtletaProvaModel(**dados) # Instanciando o objeto
        try:
            atleta_prova.save_atleta_prova()
        except:
            return {"message": "Ocorreu um erro intero ao cadastrar atleta_prova '{}'.".format(dados['id'])}, 500
        return atleta_prova.json(), 201 # created


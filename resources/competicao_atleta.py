from flask_restful import Resource, reqparse
from models.competicao_atleta import CompeticaoAtletaModel

atributos = reqparse.RequestParser()
atributos.add_argument('id_competicao', type=str, required=True, help="O campo id_competicao não pode ser vazio.")
atributos.add_argument('id_atleta', type=str, required=True, help="O campo id_atleta não pode ser vazio.")
atributos.add_argument('resultado_1', type=str)
atributos.add_argument('resultado_2', type=str)
atributos.add_argument('resultado_3', type=str)

class CompeticoesAtletas(Resource):
    # pass
    # /competicoes_atletas
    def get(self):
        return {'competicoes_atletas': [competicao.json() for competicao in CompeticaoAtletaModel.query.all()]}

class CompeticaoAtleta(Resource):
    pass
#     # /competicoes_atletas/{id}
#     def get(self, id_competicao, id_atleta):
#         competicao_atleta = CompeticaoAtletaModel.find_competicao_atleta(id_competicao, id_atleta)
#         if competicao_atleta: # = if competicao_atleta is not null
#             return competicao_atleta.json()
#         return {"message": "competicao_atleta '{} e {}' não encontrada.".format(id_competicao, id_atleta)}, 404 #status code not found
    

#     def put(self, id_competicao, id_atleta):
#         dados = atributos.parse_args()
#         competicao_atleta_encontrada = CompeticaoAtletaModel.find_competicao_atleta(id_competicao, id_atleta)
#         if competicao_atleta_encontrada:
#             competicao_atleta_encontrada.update_competicao_atleta(**dados)
#             competicao_atleta_encontrada.save_competicao_atleta()
#             return competicao_atleta_encontrada.json(), 200 # OK
#         competicao_atleta = CompeticaoAtletaModel(id_competicao, id_atleta, **dados) # Cria a instancia competicao_atleta
#         try:
#             competicao_atleta.save_competicao_atleta()
#         except:
#             return {"message": "Ocorreu um erro interno ao salvar os dados de competicao_atleta '{} e {}'.".format(id_competicao, id_atleta)}, 500 # Internal Server Error}
#         return competicao_atleta.json(), 201 # created


#     def delete(self, id_competicao, id_atleta):
#         competicao_atleta = CompeticaoAtletaModel.find_competicao_atleta(id_competicao, id_atleta)
#         if competicao_atleta:
#             try: 
#                 competicao_atleta.delete_competicao_atleta()
#             except:
#                 return {"message": "Ocorreu um erro intero ao tentar deletar os dados de competicao_atleta '{} e {}'.".format(id_competicao, id_atleta)}, 500 # Internal Server Error}
#             return {"message": "competicao_atleta '{} e {}' deletada.".format(id_competicao, id_atleta)}, 200 # OK
#         return {"message": "competicao_atleta '{} e {}' não encontrada.".format(id_competicao, id_atleta)}, 404


class Competicao_AtletaCadastro(Resource):
    pass
#     # /competicoes_atletas/cadastro
#     def post(self):
#         dados = atributos.parse_args()
#         if CompeticaoAtletaModel.find_by_name(dados['id_competicao, id_atleta']):
#             return {"message": "A competicao_atleta '{} e {}' já existe.".format(dados['id_competicao, id_atleta'])}, 400 # bad request       
#         competicao_atleta = CompeticaoAtletaModel(**dados) # Instanciando o objeto
#         try:
#             competicao_atleta.save_competicao_atleta()
#         except:
#             return {"message": "Ocorreu um erro intero ao cadastrar a competicao_atleta '{} e {}'.".format(dados['id_competicao, id_atleta'])}, 500
#         return competicao_atleta.json(), 201 # created


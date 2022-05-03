from datetime import datetime
from flask_restful import Resource, reqparse
from models.competicao import CompeticaoModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="O campo Nome não pode ser vazio.")
# atributos.add_argument('data_inicio', type=datetime, required=True, help="O campo data_inicio não pode ser vazio.")
atributos.add_argument('data_inicio', type=datetime, required=False)
atributos.add_argument('data_final', type=datetime, required=False)
atributos.add_argument('sexo', type=str, required=True, help="O campo sexo não pode ser vazio.")
atributos.add_argument('paralimpico', type=str, required=True, help="O campo Paralimpico não pode ser vazio.")
atributos.add_argument('id_prova', type=str, required=True, help="Toda competição precisa estar linkada com uma prova.")

class Competicoes(Resource):
    # /competicoes
    def get(self):
        return {'competicoes': [competicao.json() for competicao in CompeticaoModel.query.all()]}

class Competicao(Resource):
    # /competicoes/{id}
    def get(self, id):
        competicao = CompeticaoModel.find_competicao(id)
        if competicao: # = if competicao is not null
            return competicao.json()
        return {"message": "Competição '{}' não encontrada.".format(id)}, 404 #status code not found
    

    def put(self, id):
        dados = atributos.parse_args()
        competicao_encontrada = CompeticaoModel.find_competicao(id)
        if competicao_encontrada:
            competicao_encontrada.update_competicao(**dados)
            competicao_encontrada.save_competicao()
            return competicao_encontrada.json(), 200 # OK
        competicao = CompeticaoModel(id, **dados) # Cria a instancia competicao
        try:
            competicao.save_competicao()
        except:
            return {"message": "Ocorreu um erro intero ao salvar os dados da competição '{}'.".format(id)}, 500 # Internal Server Error}
        return competicao.json(), 201 # created


    def delete(self, id):
        competicao = CompeticaoModel.find_competicao(id)
        if competicao:
            try: 
                competicao.delete_competicao()
            except:
                return {"message": "Ocorreu um erro intero ao tentar deletar os dados da competição '{}'.".format(id)}, 500 # Internal Server Error}
            return {"message": "Competição '{}' deletada.".format(id)}, 200 # OK
        return {"message": "Competição '{}' não encontrada.".format(id)}, 404


class CompeticaoCadastro(Resource):
    # /competicoes/cadastro
    def post(self):
        dados = atributos.parse_args()
        if CompeticaoModel.find_by_name(dados['nome']):
            return {"message": "A competição '{}' já existe.".format(dados['nome'])}, 400 # bad request       
        competicao = CompeticaoModel(**dados) # Instanciando o objeto
        try:
            competicao.save_competicao()
        except:
            return {"message": "Ocorreu um erro interno ao cadastrar a competição '{}'.".format(dados['nome'])}, 500
        return competicao.json(), 201 # created


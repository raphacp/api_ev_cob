from flask_restful import Resource, reqparse
import mysql.connector

def normalize_path_params (id = 2,
                            nome = 'Jermaine Anderson',
                            pais = 'Espanha',
                            sexo = 'Masculino',
                            paralimpico = 'Nao',
                            limit = 50,
                            offset = 0, **dados):
#     if pais:
        return {
                'id': id,
                'nome': nome,
                'pais': pais,
                'sexo': sexo,
                'paralimpico,': paralimpico,
                'limit': limit,
                'offset': offset
                }

# path /competicoes?evento=Copa 1&id_prova=1&bateria=Final&sexo=Masculino&paralimpico=Nao
#recebe os parametros passados na url
path_params = reqparse.RequestParser()
path_params.add_argument('id',  type=int)
path_params.add_argument('nome', type=str)
path_params.add_argument('pais', type=str)
path_params.add_argument('sexo', type=str)
path_params.add_argument('paralimpico', type=str)
# path_params.add_argument('limit', type=int)
# path_params.add_argument('offset', type=int)


class Consulta_Atletas(Resource):
    # /consultas/atletas
    def get(self):
        connection = mysql.connector.connect(user='root', password='Cedes010', host='localhost', database='api_ev_cob')
        cursor = connection.cursor()

        dados = path_params.parse_args() # Recebe todos os parametros de path_params. Coloca null para os vazios
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} # Recebe somente os valores passados na url, remove os vazios
        # parametros = normalize_path_params(**dados_validos) # Chama a função que ja tem valores padroes definidos. Caso algum valor tenha sido passado na url, eles vão substituir os padroes
        
        id = dados_validos.get('id')
        nome = dados_validos.get('nome')
        pais = dados_validos.get('pais')
        sexo = dados_validos.get('sexo')
        paralimpico = dados_validos.get('paralimpico')

        consulta_sql = '''SELECT * FROM atleta WHERE'''
        filtro = []

        if id:
            consulta_sql += ' id= %s AND'
            filtro.append(id)
        if nome:
            consulta_sql += ' nome= %s AND'
            filtro.append(nome)
        if pais:
            consulta_sql += ' pais= %s AND'
            filtro.append(pais)
        if sexo:
            consulta_sql += ' sexo= %s AND'
            filtro.append(sexo)
        if paralimpico:
            consulta_sql += ' paralimpico= %s AND'
            filtro.append(paralimpico)
        if not (id or nome or pais or sexo or paralimpico):
            return {"message": "Atributos não informados."}, 404 #status code not found

        consulta_sql = consulta_sql[:-4] + ';'

        tupla = tuple([dados_validos[chave] for chave in dados_validos])
        
        cursor.execute(consulta_sql, tupla)
        resultado = cursor.fetchall()

        atletas = []
        for linha in resultado:
            atletas.append({
            'id': linha[0] ,
            'nome': linha[1],
            'pais': linha[2],
            'sexo': linha[3],
            'paralimpico': linha[4],
            })

        return {'atletas': atletas}

   

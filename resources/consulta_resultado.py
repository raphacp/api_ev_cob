from flask_restful import Resource, reqparse
import mysql.connector
import json
import datetime

# Serializando o tipo datetime pq o json nao aceita datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(campo_data):
        if isinstance(campo_data, datetime.datetime):
            return (str(campo_data))
        else:
            return super().default(campo_data)

# path /resultados?evento=Copa 1&id_prova=1&bateria=Final&sexo=Masculino&paralimpico=Nao
#recebe os parametros passados na url
path_params = reqparse.RequestParser()
path_params.add_argument('evento',  type=str)
path_params.add_argument('id_prova', type=int)
path_params.add_argument('bateria', type=str)
path_params.add_argument('id_competicao', type=int)
path_params.add_argument('sexo', type=str)
path_params.add_argument('paralimpico', type=str)
# path_params.add_argument('limit', type=float)
# path_params.add_argument('offset', type=float)


class Consulta_Resultados(Resource):
    # /consultas/resultados
    def get(self):
        connection = mysql.connector.connect(user='root', password='Cedes010', host='localhost', database='api_ev_cob')
        cursor = connection.cursor()

        dados = path_params.parse_args() # Recebe todos os parametros de path_params. Coloca null para os vazios
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} # Recebe somente os valores passados na url, remove os vazios
        # parametros = normalize_path_params(**dados_validos) # Chama a função que ja tem valores padroes definidos. Caso algum valor tenha sido passado na url, eles vão substituir os padroes
        
        evento = dados_validos.get('evento')
        id_prova = dados_validos.get('id_prova')
        bateria = dados_validos.get('bateria')
        id_competicao = dados_validos.get('id_competicao')
        sexo = dados_validos.get('sexo')
        paralimpico = dados_validos.get('paralimpico')

        consulta_sql = '''SELECT * FROM competicao_prova_atleta WHERE'''
        filtro = []

        if evento:
            consulta_sql += ' evento= %s AND'
            filtro.append(evento)
        if id_prova:
            consulta_sql += ' id_prova= %s AND'
            filtro.append(id_prova)
        if bateria:
            consulta_sql += ' bateria= %s AND'
            filtro.append(bateria)
        if id_competicao:
            consulta_sql += ' id_competicao= %s AND'
            filtro.append(id_competicao)
        if sexo:
            consulta_sql += ' sexo= %s AND'
            filtro.append(sexo)
        if paralimpico:
            consulta_sql += ' paralimpico= %s AND'
            filtro.append(paralimpico)
        if not (evento or id_prova or bateria or id_competicao or sexo or paralimpico):
            return {"message": "Atributos não informados."}, 404 #status code not found

        consulta_sql = consulta_sql[:-4] + ';'

        tupla = tuple([dados_validos[chave] for chave in dados_validos])
        
        cursor.execute(consulta_sql, tupla)
        resultado = cursor.fetchall()

        resultados = []
        for linha in resultado:
            resultados.append({
            'evento': linha[0] ,
            'id_prova': linha[1],
            'prova': linha[2],
            'unidade_medida': linha[3],
            'id_competicao': linha[4],
            'competicao': linha[5],
            'sexo': linha[6],
            'paralimpico': linha[7],
            'bateria': linha[8],
            'data_inicio': json.dumps(linha[9], default=DateTimeEncoder.default), # Serializando o tipo datetime pq o json nao aceita datetime
            'data_final': json.dumps(linha[10], default=DateTimeEncoder.default), # Serializando o tipo datetime pq o json nao aceita datetime,
            'id_atleta': linha[11],
            'atleta': linha[12],
            'pais': linha[13],
            'resultado_1': linha[14],
            'resultado_2': linha[15],
            'resultado_3': linha[16],
            'maior_resultado': linha[17]
            })

        return {'resultados': resultados}



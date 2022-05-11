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

# path /consultas/ranking?evento=Copa 1&id_prova=1&bateria=Final&sexo=Masculino&paralimpico=Nao
#recebe os parametros passados na url
path_params = reqparse.RequestParser()
path_params.add_argument('id_competicao', type=int)


class Consulta_Ranking(Resource):
    # /consultas/ranking
    def get(self):
        connection = mysql.connector.connect(user='root', password='Cedes010', host='localhost', database='api_ev_cob')
        cursor = connection.cursor()

        dados = path_params.parse_args() # Recebe todos os parametros de path_params. Coloca null para os vazios
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None} # Recebe somente os valores passados na url, remove os vazios
                
        id_competicao = dados_validos.get('id_competicao')

        if not (id_competicao):
            return {"message": "Atributo 'id_competicao' não informado."}, 404 #status code not found

        # Executa a consulta sem ordenação
        consulta_sql = f'''SELECT * FROM competicao_prova_atleta WHERE id_competicao = {id_competicao};'''
        cursor.execute(consulta_sql)
        resultado = cursor.fetchall()

        # Pega o campo unidade_medida
        unidade_de_medida = resultado[0][3]

        # Verifica a unidade de medida para selecionar a ordenação da lista. s = ascendente (100m), m = descendente (dardo)
        if unidade_de_medida == 's':
            consulta_sql = f'''SELECT * FROM competicao_prova_atleta WHERE id_competicao = {id_competicao} ORDER BY maior_resultado ASC;'''
        elif unidade_de_medida == 'm':
            consulta_sql = f'''SELECT * FROM competicao_prova_atleta WHERE id_competicao = {id_competicao} ORDER BY maior_resultado DESC;'''

        # Executa a consulta com ordenação
        cursor.execute(consulta_sql)
        resultado_ordenado = cursor.fetchall()

        ranking = []
        for linha in resultado_ordenado:
            ranking.append({
            'evento': linha[0],
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

        return {'ranking': ranking}



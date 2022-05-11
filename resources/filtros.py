

# Define os valores padroes. Caso o usuario passe algum valor em **dados ele ira substituir o padrão
def normalize_path_params(evento = None,
                          prova = None,
                          bateria = None,
                          competicao = None,
                          sexo = None,
                          paralimpico = None,
                          limit = 50,
                          offset = 0, **dados):
    if competicao:
        return {
                'evento': evento,
                'prova': prova,
                'bateria': bateria,
                'competicao': competicao,
                'sexo': sexo,
                'paralimpico,': paralimpico,
                'limit': limit,
                'offset': offset
                }
    return {
            'evento': evento,
            'prova': prova,
            'bateria': bateria,
            'sexo': sexo,
            'paralimpico,': paralimpico,
            'limit': limit,
            'offset': offset
            }

consulta_sem_competicao = "SELECT * FROM hoteis \
                        WHERE (estrelas >= ? and estrelas <= ?) \
                        and (diaria >= ? and diaria <= ?) \
                        LIMIT ? OFFSET ?"

consulta_com_competicao = "SELECT * FROM hoteis \
                        WHERE (estrelas >= ? and estrelas <= ?) \
                        and (diaria >= ? and diaria <= ?) \
                        and cidade = ? LIMIT ? OFFSET ?"


                        
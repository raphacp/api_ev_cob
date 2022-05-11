Construir uma API REST em Python para o COB (Comitê Olímpico Brasileiro)

https://github.com/raphacp/api_ev_cob

Ferramentas utilizadas no desenvolvimento da API:
	Python 3.10.4
	Flask 2.1.1
	MySQL Workbench 8.0.29
	Postman

A documentação da API foi feita no Postman e está disponível on-line
	https://documenter.getpostman.com/view/20768344/UyxgJnkg

Procedimento de instalação:
1 - Descompactar o projeto

2 - Importar as bibliotecas
	    pip install -r requirements.txt
	
3 - Informar os parâmetros de banco (usuário, senha, host, nome) nos arquivos:
	    .\app.py
	    .\resources\consulta_atleta.py
	    .\resources\consulta_ranking.py
	    .\resources\consulta_resultado.py
	
4 - Executar a aplicação.
	    Executar o arquivo .\app.py
	    Após fazer a primeira requisição será criado o banco, as tabelas e a view
	    Caso queira, pode executar o script insert_api_ev_cob.sql, que está na pasta .\banco. Ele vai inserir dados em todas as tabelas.
	
5 - Utilizei o Postman para testar a API.
	    A coleção está em .\postman\APP_EV_COB.postman_collection.json

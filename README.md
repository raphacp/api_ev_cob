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


Utilização do ambiente virtual no Python (virtualenv) com Windows 11 e VSCode

Abrir o VSCode na pasta onde está o projeto. No meu caso é: "C:\Python\api_ev_cob"
Abrir o terminal do VSCode
Instalar a biblioteca virtualenv
	pip install virtualenv
Criar o ambiente virtual (ambvir é o nome do ambiente virtual que estou criando)
	C:\Python\api_ev_cob>virtualenv ambvir --python=python3.10
Ativar o ambiente virtual no Windows:
	.\ambvir\Scripts\activate.bat
	Ele entra no ambiente virtual. "(ambvir) C:\Python\api_ev_cob>"
	
****************************************************
Pode ser que o comando .\ambvir\Scripts\activate.bat para ativar o Ambiente Virtual no Windows, não funcione. Caso isso ocorra, utilize o comando: 			
	\NomeDoAmbienteVirtual\Scripts\activate.ps1

Se tiver problemas de acesso não autorizado, execute: 
	Set-ExecutionPolicy Unrestricted -Scope Process
e tente novamente. Esse comando autoriza a execução desse comando apenas no powershell aberto.

Certifique-se de executar esse comando no powershell.
****************************************************
	
Ao digitar pip freeze poderá verificar que o ambiente está "zerado"
Instalar as bibliotecas necessárias
	pip install -r requirements.txt
	
Executar a aplicação
	python app.py

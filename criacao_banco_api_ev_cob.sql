-- Criação do banco de dados

CREATE DATABASE api_ev_cob;

USE api_ev_cob;

-- Criação da tabela Atleta
CREATE TABLE Atleta(
Id INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(150) NOT NULL,
Pais VARCHAR(100) NOT NULL,
Sexo ENUM("Masculino", "Feminino"),
-- Paralimpico BOOL NOT NULL DEFAULT FALSE, # Fiquei na dúvida qual seria mais apropriado
Paralimpico ENUM("Sim", "Nao"),
PRIMARY KEY (Id)
);

-- Criação da tabela Modalidade
CREATE TABLE Modalidade(
Id INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(150) NOT NULL,
PRIMARY KEY (Id)
);

-- Criação da tabela Prova
CREATE TABLE Prova(
Id INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(150) NOT NULL,
Unidade_Medida ENUM("s", "m"),
Id_Modalidade INT NOT NULL,
PRIMARY KEY (Id),
FOREIGN KEY (Id_Modalidade) REFERENCES Modalidade(Id)
);

-- Criação da tabela Competicao
CREATE TABLE Competicao(
Id INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(150) NOT NULL,
Data_Inicio DATETIME NOT NULL,
Data_Final DATETIME,
Tipo ENUM("Masculino", "Feminino"),
Paralimpico ENUM("Sim", "Nao"),
Id_Prova INT NOT NULL,
PRIMARY KEY (Id),
FOREIGN KEY (Id_Prova) REFERENCES Prova(Id)
);

-- Criação da tabela Competicao_Atleta
CREATE TABLE Competicao_Atleta(
Id_Competicao INT NOT NULL,
Id_Atleta INT NOT NULL,
Resultado_1 FLOAT,
Resultado_2 FLOAT,
Resultado_3 FLOAT,
PRIMARY KEY (Id_Competicao, Id_ATleta),
FOREIGN KEY (Id_Competicao) REFERENCES Competicao(Id),
FOREIGN KEY (Id_Atleta) REFERENCES Atleta(Id)
);
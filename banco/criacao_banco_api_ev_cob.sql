-- Criação do banco de dados

CREATE DATABASE api_ev_cob;

USE api_ev_cob;

-- Criação da tabela Atleta
CREATE TABLE Atleta(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(150) NOT NULL,
pais VARCHAR(100) NOT NULL,
sexo ENUM("Masculino", "Feminino"),
paralimpico ENUM("Sim", "Nao"),
PRIMARY KEY (id)
);

-- Criação da tabela Modalidade
CREATE TABLE Modalidade(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(150) NOT NULL,
PRIMARY KEY (id)
);

-- Criação da tabela Prova
CREATE TABLE Prova(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(150) NOT NULL,
unidade_medida ENUM("s", "m"),
id_modalidade INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id)
);

-- Criação da tabela Competicao
CREATE TABLE Competicao(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(150) NOT NULL,
data_inicio DATETIME NOT NULL,
data_final DATETIME,
sexo ENUM("Masculino", "Feminino"),
paralimpico ENUM("Sim", "Nao"),
id_prova INT NOT NULL,
evento VARCHAR(150) NOT NULL,
tipo_bateria VARCHAR(150) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id_prova) REFERENCES Prova(id)
);

-- Criação da tabela Competicao_Atleta
CREATE TABLE Competicao_Atleta(
id INT NOT NULL AUTO_INCREMENT,
id_competicao INT NOT NULL,
id_atleta INT NOT NULL,
resultado_1 FLOAT,
resultado_2 FLOAT,
resultado_3 FLOAT,
PRIMARY KEY (id),
FOREIGN KEY (id_competicao) REFERENCES Competicao(id),
FOREIGN KEY (id_atleta) REFERENCES Atleta(id),
CONSTRAINT competicao_atleta UNIQUE (id_competicao, id_atleta)
);

-- Criação da tabela Atleta_Prova
CREATE TABLE Atleta_Prova(
id INT NOT NULL AUTO_INCREMENT,
id_atleta INT NOT NULL,
id_prova INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id_atleta) REFERENCES Atleta(id),
FOREIGN KEY (id_prova) REFERENCES Prova(id),
CONSTRAINT atleta_prova UNIQUE (id_atleta, id_prova)
);

CREATE OR REPLACE VIEW competicao_prova_atleta AS
SELECT c.evento, c.id_prova, p.nome as prova, p.unidade_medida, c.id as id_competicao, c.nome as competicao, c.sexo, c.paralimpico, c.tipo_bateria as bateria, 
c.data_inicio, c.data_final, a.id as id_atleta, a.nome as atleta, a.pais, ca.resultado_1, ca.resultado_2, ca.resultado_3, GREATEST(IFNULL(resultado_1, 0), 
IFNULL(resultado_2, 0), IFNULL(resultado_3, 0)) as maior_resultado
FROM competicao c, prova p, competicao_atleta ca, atleta a
WHERE c.id_prova = p.id and ca.id_competicao = c.id and ca.id_atleta = a.id;


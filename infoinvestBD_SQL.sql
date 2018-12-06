CREATE TABLE Cambio (
	id serial,
	tipo_moeda VARCHAR(20) NOT NULL,
	valor FLOAT NOT NULL,
	data date NOT NULL,
	data_cadastro timestamp NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(data_cadastro)
);

CREATE TABLE Indice (
	id serial,
	nome VARCHAR(100) NOT NULL,
	taxa FLOAT NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(nome)
);

CREATE TABLE Perfil (
	id serial,
	tipo_perfil VARCHAR(20) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(tipo_perfil)
);
CREATE TABLE Usuario (
	cpf VARCHAR(11),
	senha VARCHAR(20) NOT NULL,
	nome VARCHAR(150) NOT NULL,
	email VARCHAR(100) NOT NULL,
	renda FLOAT,
	id_perfil serial,
	PRIMARY KEY(cpf),
	UNIQUE(email),
	FOREIGN KEY (id_perfil) REFERENCES Perfil(id)
);

CREATE TABLE Tipo_investimento (
	id serial,
	nome VARCHAR(50) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(nome)	
);

CREATE TABLE Cadastro_investimento (
	codigo serial,
	saldo FLOAT,
	data_aplicacao date NOT NULL,
	data_retirada date,
	cpf_usuario VARCHAR(11),
	tipo_id serial,
	PRIMARY KEY(codigo),
	FOREIGN KEY (cpf_usuario) REFERENCES Usuario(cpf),
	FOREIGN KEY (tipo_id) REFERENCES Tipo_investimento(id)
);
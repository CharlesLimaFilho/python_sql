CREATE DATABASE IF NOT EXISTS ingressos;
USE ingressos;

CREATE TABLE endereco (
  id_endereco INT AUTO_INCREMENT PRIMARY KEY,
  rua VARCHAR(100),
  numero VARCHAR(10),
  cidade VARCHAR(50),
  estado CHAR(20)
);

CREATE TABLE cliente (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  id_endereco INT NOT NULL,
  celular VARCHAR(20) NOT NULL,
  FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE setor (
  id_setor INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL UNIQUE,
  valor_base DECIMAL(10,2) NOT NULL
);

CREATE TABLE tipo_ingresso (
  id_tipo INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(20) NOT NULL UNIQUE,
  fator DECIMAL(3,2) NOT NULL
);

CREATE TABLE evento (
  id_evento INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  data DATE NOT NULL,
  id_endereco INT NOT NULL,
  limite_ingressos_por_cpf INT NOT NULL,
  FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE ingresso (
  id_ingresso INT AUTO_INCREMENT PRIMARY KEY,
  id_evento INT NOT NULL,
  id_cliente INT NOT NULL,
  id_setor INT NOT NULL,
  id_tipo INT NOT NULL,
  preco_final DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_evento) REFERENCES evento(id_evento),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
  FOREIGN KEY (id_setor) REFERENCES setor(id_setor),
  FOREIGN KEY (id_tipo) REFERENCES tipo_ingresso(id_tipo)
);
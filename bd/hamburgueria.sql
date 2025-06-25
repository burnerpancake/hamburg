CREATE DATABASE bd_hamburgueria;

USE bd_hamburgueria;

CREATE TABLE IF NOT EXISTS cliente(
	id int PRIMARY KEY AUTO_INCREMENT,
	nome varchar(30) not null,
	sobrenome varchar(30) not null,
	telefone varchar(14) not null,
	email varchar(60) not null,
	cpf varchar(11)
);

CREATE TABLE IF NOT EXISTS fornecedor(
	id int PRIMARY KEY AUTO_INCREMENT,
	nome varchar(30) not null,
	sobrenome varchar(30) not null,
	telefone varchar(14) not null,
	email varchar(60) not null,
	registro varchar(14) nit null
);
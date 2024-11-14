DROP DATABASE IF EXISTS criptomonedas;

CREATE DATABASE criptomonedas; 

USE criptomonedas;

DROP TABLE IF EXISTS criptos;

CREATE TABLE criptos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(20) NOT NULL,
    VALOR FLOAT,
    FECHA DATE
);
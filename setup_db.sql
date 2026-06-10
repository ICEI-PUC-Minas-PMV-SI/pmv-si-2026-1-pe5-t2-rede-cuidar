-- Executar no MySQL do Ubuntu Server
CREATE DATABASE IF NOT EXISTS hospital_cuidar CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'cuidar_user'@'localhost' IDENTIFIED BY 'cuidar_pass';
GRANT ALL PRIVILEGES ON hospital_cuidar.* TO 'cuidar_user'@'localhost';
FLUSH PRIVILEGES;

USE hospital_cuidar;

CREATE TABLE IF NOT EXISTS pacientes (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    nome             VARCHAR(150) NOT NULL,
    cpf              VARCHAR(14)  NOT NULL,
    data_nascimento  DATE         NOT NULL,
    unidade          VARCHAR(50)  NOT NULL,
    criado_em        TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

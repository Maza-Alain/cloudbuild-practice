-- Crear la base de datos algoritmosOrdenamiento si no existe
CREATE DATABASE IF NOT EXISTS algoritmosOrdenamiento;

-- Usar la base de datos algoritmosOrdenamiento
USE algoritmosOrdenamiento;

-- Crear la tabla Consultas
CREATE TABLE Consultas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(255) NOT NULL,
    tiempo FLOAT NOT NULL,
    largoLista INT NOT NULL
);

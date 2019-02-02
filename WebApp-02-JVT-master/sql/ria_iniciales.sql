CREATE DATABASE ria_iniciales;

USE ria_iniciales;

CREATE TABLE clientes(
	nombre varchar(50) NOT NULL PRIMARY KEY,
	ap_paterno varchar(50) NOT NULL,
	ap_materno varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	direccion varchar(50) NOT NULL
)ENGINE = InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos(
	nombre_p varchar(50)	NOT NULL PRIMARY KEY,
	categoria varchar(50) NOT NULL,
	descripcion varchar(50) NOT NULL,
	marca varchar(50) NOT NULL,
	cantidad varchar (15) NOT NULL
)ENGINE = InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(nombre,ap_paterno,ap_materno,email,direccion)
VALUES ('Jonatan','Vazquez','Tellez','jona@gmail','chamizal'),
('Marleny','Bonilla','Franco','mar@gmail','caltengo'),
('Azul','Lozada','Estrada','anzu@gmail','Fresnos');

INSERT INTO productos(nombre_p,categoria,descripcion,marca,cantidad)
VALUES ('escoba','limpieza','escoba para limpieza','bruja','diez'),
('queso','lacteo','queso cotage','alpura','seis'),
('catsup','salsas','puro tomate','monte','tres');

SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
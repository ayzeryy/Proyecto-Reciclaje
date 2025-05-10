CREATE DATABASE reciclaje_db;
USE reciclaje_db;
show tables;
DESCRIBE botes;
DESCRIBE residuos;
DESCRIBE puntos;


ALTER TABLE usuarios
ADD COLUMN es_admin BOOLEAN DEFAULT FALSE;
SELECT * FROM usuarios;
SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'reciclaje_db' AND TABLE_NAME = 'residuos';


CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL, 
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE residuos (
    id_residuo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) UNIQUE NOT NULL,
    descrDipcion TEXT,
    id_bote INT NOT NULL,
    FOREIGN KEY (id_bote) REFERENCES botes(id_bote) ON DELETE CASCADE
);

CREATE TABLE botes (
    id_bote INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    color VARCHAR(50)
);

CREATE TABLE puntos (
    id_puntos INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    fecha_otorgado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);


CREATE TABLE historial_busqueda (
    id_historial INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_residuo INT NOT NULL,
    fecha_busqueda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_residuo) REFERENCES residuos(id_residuo) ON DELETE CASCADE
);

INSERT INTO botes (nombre, color) VALUES
('Orgánico', 'Verde'),
('Inorgánico', 'Gris'),
('Reciclable', 'Azul'),
('Papel y cartón', 'Café'),
('Vidrio', 'Blanco');

SELECT * FROM botes;
DESCRIBE residuos;
ALTER TABLE residuos CHANGE descrDipcion descripcion TEXT;

INSERT INTO residuos (nombre, descripcion, id_bote) VALUES
('manzana', 'Restos de fruta, biodegradable', 1),
('botella plastica', 'Botellas PET reciclables', 3),
('papel', 'Hojas de papel limpio', 4),
('vidrio', 'Envases de vidrio', 5),
('lata', 'Latas de aluminio reciclables', 3);

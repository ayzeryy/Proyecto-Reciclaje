-- Crear base de datos
CREATE DATABASE IF NOT EXISTS reciclaje_db;
USE reciclaje_db;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    es_admin BOOLEAN DEFAULT FALSE
);

-- Tabla de botes
CREATE TABLE IF NOT EXISTS botes (
    id_bote INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    color VARCHAR(50)
);

-- Tabla de residuos
CREATE TABLE IF NOT EXISTS residuos (
    id_residuo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) UNIQUE NOT NULL,
    descripcion TEXT,
    id_bote INT NOT NULL,
    FOREIGN KEY (id_bote) REFERENCES botes(id_bote) ON DELETE CASCADE
);

-- Tabla de puntos
CREATE TABLE IF NOT EXISTS puntos (
    id_puntos INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    fecha_otorgado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabla de historial de búsqueda
CREATE TABLE IF NOT EXISTS historial_busqueda (
    id_historial INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_residuo INT NOT NULL,
    fecha_busqueda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_residuo) REFERENCES residuos(id_residuo) ON DELETE CASCADE
);

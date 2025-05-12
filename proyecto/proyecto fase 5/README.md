# Proyecto de Reciclaje 

Este es un programa en Python que permite:
- Registrar usuarios con roles (usuario o administrador).
- Iniciar sesión.
- Buscar residuos y ver en qué bote deben depositarse.
- Ganar puntos por búsquedas e inicios de sesión.
- Ver puntos acumulados (últimos 30 días).
- Administrar residuos y ver tablas (solo administradores).

## Requisitos
- Python 3.11+
- MySQL
- mysql-connector-python

## Estructura del Proyecto
- `main.py`: Menú principal del programa.
- `usuarios.py`: Registro e inicio de sesión.
- `puntos.py`: Registro de puntos por actividad.
- `residuos.py`: Agregar residuos (solo admin).
- `busqueda.py`: Buscar residuos y registrar historial.
- `mostrar.py`: Mostrar tablas (solo admin).
- `db_conexion.py`: Conexión a la base de datos.
- `estructura.sql`: Script para crear la base de datos y tablas.

## Instrucciones de uso
1. Clona este repositorio o descarga el ZIP.
2. Configura tus credenciales en `db_conexion.py`.
3. Ejecuta `estructura.sql` en tu base de datos MySQL.
4. Corre `main.py` para iniciar el sistema.

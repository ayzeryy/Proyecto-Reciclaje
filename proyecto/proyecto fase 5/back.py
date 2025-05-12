import mysql.connector
from mysql.connector import Error

def mostrar_tablas():
    try:
        
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Janpapi741A@1",
            database="reciclaje_db"
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SHOW TABLES;")

            print("Tablas en la base de datos 'reciclaje':")
            for tabla in cursor.fetchall():
                print(f"- {tabla[0]}")

            cursor.close()
            conexion.close()

    except Error as e:
        print("Error al conectar o consultar la base de datos:", e)

# Ejecutar
mostrar_tablas()


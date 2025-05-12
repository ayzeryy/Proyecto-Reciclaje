from db_conexion import conectar

def mostrar_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SHOW TABLES;")
    print("Tablas en la base de datos:")
    for tabla in cursor.fetchall():
        print(f"- {tabla[0]}")

    #cursor.close()
    #conexion.close()

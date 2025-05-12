from db_conexion import conectar
from puntos import asignar_punto

def buscar_residuo(id_usuario):
    residuo_nombre = input("Ingrese el nombre del residuo a buscar: ").strip().lower()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT r.id_residuo, r.nombre, b.nombre, b.color
        FROM residuos r
        JOIN botes b ON r.id_bote = b.id_bote
        WHERE LOWER(r.nombre) = %s
    """, (residuo_nombre,))

    resultado = cursor.fetchone()

    if resultado:
        id_residuo, nombre_residuo, nombre_bote, color_bote = resultado
        print(f"El residuo '{nombre_residuo}' va en el bote '{nombre_bote}' de color {color_bote}.")

        
        cursor.execute("""
            INSERT INTO historial_busqueda (id_usuario, id_residuo)
            VALUES (%s, %s)
        """, (id_usuario, id_residuo))

        
        asignar_punto(id_usuario)

        conexion.commit()
    else:
        print("Residuo no encontrado en la base de datos.")

    #cursor.close()
    #conexion.close()

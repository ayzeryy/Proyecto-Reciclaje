from db_conexion import conectar

def asignar_punto(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO puntos (id_usuario, cantidad)
        VALUES (%s, 1)
    """, (id_usuario,))

    conexion.commit()
    cursor.close()
    conexion.close()
    print("Se asignó 1 punto por inicio de sesión.")

def ver_puntos_actuales(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT SUM(cantidad) FROM puntos
        WHERE id_usuario = %s
        AND fecha_otorgado >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    """, (id_usuario,))

    resultado = cursor.fetchone()
    puntos = resultado[0] if resultado[0] is not None else 0

    #cursor.close()
    #conexion.close()

    return puntos
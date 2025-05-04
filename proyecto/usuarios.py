from db_conexion import conectar
from puntos import asignar_punto


def registrar_usuario():
    correo = input("Ingrese su correo: ").strip().lower()
    contraseña = input("Ingrese su contraseña: ").strip()
    es_admin = input("¿Este usuario es administrador? (s/n): ").strip().lower() == "s"

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    existente = cursor.fetchone()

    if existente is None:
        cursor.execute(
            "INSERT INTO usuarios (correo, contraseña, es_admin) VALUES (%s, %s, %s)",
            (correo, contraseña, es_admin)
        )
        conexion.commit()
        print("Usuario registrado exitosamente.")
    else:
        print("El correo ya está registrado.")

    cursor.close()
    conexion.close()

def iniciar_sesion():
    correo = input("Correo: ").strip().lower()
    contraseña = input("Contraseña: ").strip()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_usuario, es_admin FROM usuarios WHERE correo = %s AND contraseña = %s", (correo, contraseña))
    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    if usuario:
        print("Inicio de sesión exitoso.")
        id_usuario, es_admin = usuario
        asignar_punto(id_usuario)
        return id_usuario, es_admin
    else:
        print("Correo o contraseña incorrectos.")
        return None, None

    #cursor.close()
    #conexion.close()

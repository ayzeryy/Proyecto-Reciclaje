from db_conexion import conectar

def agregar_residuo():
    nombre = input("Nombre del residuo: ").strip().lower()
    descripcion = input("Descripción del residuo: ").strip()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_bote, nombre, color FROM botes")
    botes = cursor.fetchall()

    print("\nBotes disponibles:")
    for bote in botes:
        print(f"{bote[0]}. {bote[1]} ({bote[2]})")

    id_bote_input = input("Ingrese el ID del bote para este residuo: ").strip()

    if id_bote_input.isdigit():
        id_bote = int(id_bote_input)

        cursor.execute("""
            INSERT INTO residuos (nombre, descripcion, id_bote)
            VALUES (%s, %s, %s)
        """, (nombre, descripcion, id_bote))

        conexion.commit()
        print("Residuo agregado correctamente.")
    else:
        print("Error: debe ingresar un número válido para el ID del bote.")

    #cursor.close()
    #conexion.close()


from db_conexion import conectar
import pandas as pd

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

        
def cargar_residuos_csv(ruta_archivo):
    df = pd.read_csv(ruta_archivo)

    conexion = conectar()
    cursor = conexion.cursor()
    agregados = 0
    omitidos = 0

    for _, fila in df.iterrows():
        cursor.execute("SELECT COUNT(*) FROM residuos WHERE nombre = %s", (fila["nombre"].strip().lower(),))
        if cursor.fetchone()[0] == 0:
            sql = "INSERT INTO residuos (nombre, descripcion, id_bote) VALUES (%s, %s, %s)"
            cursor.execute(sql, (
                fila["nombre"].strip().lower(), 
                fila["descripcion"], 
                int(fila["id_bote"])
            ))
            agregados += 1
        else:
            omitidos += 1
            print(f" '{fila['nombre']}' ya existe. Se omitió.")

    conexion.commit()
    conexion.close()

    print(f"\nSe agregaron {agregados} residuos nuevos.")
    print(f"Se omitieron {omitidos} residuos duplicados.")


    #cursor.close()
    #conexion.close()


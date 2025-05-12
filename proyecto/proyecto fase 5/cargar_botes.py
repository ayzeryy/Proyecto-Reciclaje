import pandas as pd
from db_conexion import conectar

df = pd.read_csv("botes_ejemplo_id_1_a_4.csv")

conexion = conectar()
cursor = conexion.cursor()

for _, fila in df.iterrows():
    cursor.execute("INSERT INTO botes (id_bote, nombre, color) VALUES (%s, %s, %s)", 
                   (int(fila["id_bote"]), fila["nombre"], fila["color"]))

conexion.commit()
conexion.close()

print(f"Se cargaron {len(df)} botes correctamente.")

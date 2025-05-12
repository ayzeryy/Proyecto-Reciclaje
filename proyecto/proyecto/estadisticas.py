from db_conexion import conectar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_estadisticas():
    conexion = conectar()

    consulta = """
    SELECT hb.fecha_busqueda, r.nombre AS residuo, b.nombre AS bote
    FROM historial_busqueda hb
    JOIN residuos r ON hb.id_residuo = r.id_residuo
    JOIN botes b ON r.id_bote = b.id_bote
    WHERE hb.fecha_busqueda >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    """
    df = pd.read_sql(consulta, conexion)

    if df.empty:
        print("No hay datos en los últimos 30 días.")
        return

    print("\nResumen de los últimos 30 días:")
    print(df.head())

    # Exportar a CSV
    nombre_archivo = "resumen_estadistico.csv"
    df.to_csv(nombre_archivo, index=False)
    print(f"\nDatos exportados exitosamente a '{nombre_archivo}'")

    # Estadísticas por residuo y bote
    print("\nCantidad por tipo de residuo:")
    print(df["residuo"].value_counts())

    print("\nCantidad por tipo de bote:")
    print(df["bote"].value_counts())

    # Gráfico de pastel por tipo de residuo
    df["residuo"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Proporción de residuos")
    plt.ylabel("")
    plt.show()

    # Gráfico de barras por uso de botes
    df["bote"].value_counts().plot(kind="bar")
    plt.title("Uso de botes")
    plt.xlabel("Bote")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    conexion.close()

def estadisticas_numpy():
    conexion = conectar()

    consulta = """
    SELECT r.nombre AS residuo
    FROM historial_busqueda hb
    JOIN residuos r ON hb.id_residuo = r.id_residuo
    WHERE hb.fecha_busqueda >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    """
    df = pd.read_sql(consulta, conexion)

    if df.empty:
        print("No hay búsquedas en los últimos 30 días.")
        return

    conteo = df["residuo"].value_counts()
    valores = conteo.values

    media = np.mean(valores)
    desviacion = np.std(valores)

    print("\nEstadísticas NumPy:")
    print("Residuos más buscados:\n", conteo)
    print(f"\nMedia de búsquedas por tipo de residuo: {media:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")

    # Exportar al mismo CSV como resumen adicional
    with open("resumen_estadistico.csv", "a", encoding="utf-8") as f:
        f.write("\n\n# Estadísticas NumPy\n")
        conteo.to_csv(f, header=["conteo"])
        f.write(f"\nMedia de búsquedas:,{media:.2f}\n")
        f.write(f"Desviación estándar:,{desviacion:.2f}\n")

    conexion.close()
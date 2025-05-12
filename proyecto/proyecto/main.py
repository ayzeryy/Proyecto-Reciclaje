from usuarios import registrar_usuario, iniciar_sesion
from mostrar import mostrar_tablas
from puntos import ver_puntos_actuales
from busqueda import buscar_residuo
from residuos import agregar_residuo
from estadisticas import generar_estadisticas
from estadisticas import estadisticas_numpy
from residuos import cargar_residuos_csv
print("Bienvenido al sistema de reciclaje")
print("1. Registrar usuario")
print("2. Iniciar sesión")
opcion = input("Elige una opción (1-2): ")

if opcion == "1":
    registrar_usuario()
elif opcion == "2":
    usuario_id, es_admin = iniciar_sesion()
    if usuario_id:
        opcion_secundaria = ""

        while opcion_secundaria != "0":
            print("\nMenú de usuario")
            print("1. Ver puntos acumulados")
            print("2. Buscar residuo")
            if es_admin:
                print("3. Mostrar tablas")
                print("4. Agregar residuo")
                print("5. Ver estadísticas y gráficas")
                print("6. Ver análisis (media/desviación)")
                print("7. Cargar residuos desde CSV")
            print("0. Cerrar sesión")

            opcion_secundaria = input("Elige una opción: ")

            if opcion_secundaria == "1":
                puntos = ver_puntos_actuales(usuario_id)
                print(f"Puntos en los últimos 30 días: {puntos}")
            elif opcion_secundaria == "2":
                buscar_residuo(usuario_id)
            elif opcion_secundaria == "3" and es_admin:
                mostrar_tablas()
            elif opcion_secundaria == "4" and es_admin:
                agregar_residuo()
            elif opcion_secundaria == "5" and es_admin:
                generar_estadisticas()
            elif opcion_secundaria == "6" and es_admin:
                estadisticas_numpy()
            elif opcion_secundaria == "7" and es_admin:
                ruta = input("Ruta del archivo CSV: ")
                cargar_residuos_csv(ruta)
            elif opcion_secundaria == "0":
                print("Sesión cerrada.")
            else:
                print("Opción no válida.")
from usuarios import registrar_usuario, iniciar_sesion
from mostrar import mostrar_tablas
from puntos import ver_puntos_actuales
from busqueda import buscar_residuo
from residuos import agregar_residuo


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
            elif opcion_secundaria == "0":
                print("Sesión cerrada.")
            else:
                print("Opción no válida.")
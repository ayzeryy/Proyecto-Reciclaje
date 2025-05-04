# Universidad del Valle de Guatemala
# Algoritmos y Programación Básica
# Luis Eduardo Gutiérrez Oliva - 25182
# Ejercicio 5 


def mostrar_menu():
    print("\n1. Agregar curso\n2. Agregar seccion\n3. Modificar horario\n4. Eliminar seccion")
    print("5. Mostrar cursos\n6. Buscar por dia\n7. Salir")
    return input("Seleccione una opción: ").strip()

def pedir(texto):
    valor = input(texto).strip()
    while not valor:
        print("Entrada vacía. Intente de nuevo.")
        valor = input(texto).strip()
    return valor # solicita entrada del usuario y asegura que no esté vacía

def agregar_curso(cursos):
    nombre = pedir("Nombre del curso: ")
    if nombre in cursos:
        print("El curso ya existe.") # agrega un nuevo curso al diccionario si es que noo existe ya
    else:
        cursos[nombre] = {}
        print("Curso agregado.") # inicia con un diccionario vacío de  las secciones

def agregar_seccion(cursos):
    nombre = pedir("Curso existente: ")
    if nombre in cursos:
        sec = pedir("Sección: ")
        if sec not in cursos[nombre]:
            hora = pedir("Horario: ")
            if isinstance(hora, str):
                cursos[nombre][sec] = hora
                print("Sección agregada.") # agrega una sección y su horario a un curso existente
            else:
                print("Error: Horario inválido.")
        else:
            print("Sección duplicada.")
    else:
        print("Curso no encontrado.")

def modificar_horario(cursos): # deja cambiar el horario de una sección existente
    nombre, sec = pedir("Curso: "), pedir("Sección: ")
    if nombre in cursos and sec in cursos[nombre]:
        nuevo = pedir("Nuevo horario: ")
        if isinstance(nuevo, str):
            cursos[nombre][sec] = nuevo
            print("Horario actualizado.")
        else:
            print("Error: Horario inválido.")
    else:
        print("Curso o sección no encontrados.")

def eliminar_seccion(cursos): # elimina una sección de un curso; si se queda vacio elimina el curso también
    nombre, sec = pedir("Curso: "), pedir("Sección: ")
    if nombre in cursos and sec in cursos[nombre]:
        del cursos[nombre][sec]
        if not cursos[nombre]:
            del cursos[nombre]
            print("Sección eliminada y curso vacío removido.")
        else:
            print("Sección eliminada.")
    else:
        print("Curso o sección no encontrados.")

def mostrar_cursos(cursos): # muestra todos los cursos que el usuario ingreso y sus secciones con horarios
    if not cursos:
        print("No hay cursos registrados.")
    for curso, secciones in cursos.items():
        print(f"\nCurso: {curso}")
        if not secciones:
            print("  Sin secciones.")
        for sec, hora in secciones.items():
            print(f"  Sección {sec}: {hora}")

def buscar_por_dia(cursos, resumen): # busca todas las secciones que tienen clases el día ingresado y las guarda en el resumen
    dia = pedir("Día a buscar: ").lower()
    encontrado = False
    for curso, secciones in cursos.items():
        for sec, hora in secciones.items():
            if hora and isinstance(hora, str) and dia in hora.lower():
                print(f"{curso} - {sec}: {hora}")
                resumen.append((curso, sec, hora))
                encontrado = True
    if not encontrado:
        print("No se encontraron secciones en ese día.")

def resumen_final(resumen): # muestra al final del programa un resumen de todas las búsquedas hechas por día
    print("\n--- Resumen de búsquedas ---")
    if not resumen:
        print("No se hicieron búsquedas.")
    else:
        for curso, sec, hora in resumen:
            print(f"{curso} - {sec}: {hora}")

def buscar_dia_wrapper(c, resumen): # función envoltorio para pasar cursos y resumen como parámetros a la búsqueda por día
    buscar_por_dia(c, resumen) # esta funcion no esta definida en el analisis y diseño, se me ocurrio agragerlo al momento de programar
                                #muestra un pequeño resumen de las secciones que tienen clases el día ingresado

def iniciar(): # función principal del programa, agregue un  curso como ejemplo para poder ejecutar el programa y hacer pruebas del menu
    cursos = {
        "Programacion 1": {
            "A": "Lunes y Miércoles 10:00-11:30"
        }
    }
    resumen_lista = [] # lista donde se guardan resultados de búsquedas por día

    acciones = { # diccionario que asocia opciones del menú con las funciones correspondientes
        "1": agregar_curso,
        "2": agregar_seccion,
        "3": modificar_horario,
        "4": eliminar_seccion,
        "5": mostrar_cursos,
        # use esta funcion (lambda) para poder pasar los cursos y el resumen como parametros a la funcion buscar_dia_wrapper
        # ya que no pude pasar argumentos directamente a la funcion de la manera normal y no quise cambiar la firma de la funcion
        # use dos argumentos: los cursos y la lista de resumen de busquedas por dia
        "6": lambda c: buscar_dia_wrapper(c, resumen_lista)
    }

    opcion = mostrar_menu()
    while opcion != "7":
        accion = acciones.get(opcion)
        if accion:
            accion(cursos)
        else:
            print("Opción inválida.")
        opcion = mostrar_menu()

    resumen_final(resumen_lista)

iniciar() # ejecuta el programa
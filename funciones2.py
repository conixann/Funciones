#7. Funciones para menú
def mostrar_menu():
    print("\n===MENÚ PRINCIPAL ===")
    print("1.VER PRODUCTOS")
    print("2.AGREGAR PRODUCTOS")
    print("3.SALIR")
def ver_productos():
    print("Lista de productos: [VACÍA]")
def agregar_productos():
    nombre=input("Nombre de el producto: ")
    print(f"{nombre} agregado correctamente!")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opc = input("Elige una opción: ")
        if opc =="1":
            ver_productos()
        elif opc =="2":
            agregar_productos()
        elif opc=="3":
            print("Hasta pronto!")
            break
        else:
            print("Opción incorrecta.")
ejecutar_menu()

#8. Función que recibe y modifica una lista:
def agregar_tarea(lista_tareas,tarea):
    lista_tareas.append(tarea)
    print(f"Tarea {tarea} agregada. ")

def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas pendientes.")
        return
    print("\nTareas pendientes:")
    for i, tarea in enumerate(lista_tareas,1):
        print(f" {i}. {tarea}")

mis_tareas = []
agregar_tarea(mis_tareas, "estudiar python")
agregar_tarea(mis_tareas, "hacer ejercicio")
agregar_tarea(mis_tareas)
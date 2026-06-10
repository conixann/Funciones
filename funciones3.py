#8. Función que recibe y modifica una lista:
def agregar_tarea(lista_tareas:list,tarea):
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
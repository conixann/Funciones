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


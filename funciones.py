#1. Función sin parámetros:
def saludar():
    print("¡Bienvenido al sistema!")

saludar()
saludar()
saludar()


#2. Función con parámetros:
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}! Bienvenido.")

saludar_usuario("Ana")
saludar_usuario("Luis")

#3. Función con retorno:
def sumar(a,b):
    resultado= a + b
    return resultado
total = sumar(5,3)
print(f"La suma es: {total}")
print(sumar(10,20))
print(sumar("hola","mundo"))

#4. Parámetros con valor por defecto:
def crear_usuario(nombre, rol="estudiante"):
    print(f"Usuario: {nombre} | rol: {rol}")

crear_usuario("Maria")
crear_usuario("Pedro","Administrador")
crear_usuario("Laura", rol="Docente")
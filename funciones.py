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

#5. Función de validación
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    return False

edad=int(input("Ingresa tu edad: "))
if es_mayor_de_edad(edad):
    print("Acceso permitido.")
else:
    print("Accesop denegado.")

#6. Función de validación compuesta
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "Mínimo 8 caracteres"
    tiene_numero=False
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero=True
    if not tiene_numero:
        return False, "Debe contener al menos un número"
    return True, "Contraseña válida"

clave=input("Crea tu contraseña: ")
valida,mensaje=validar_contrasena(clave)
print(mensaje)
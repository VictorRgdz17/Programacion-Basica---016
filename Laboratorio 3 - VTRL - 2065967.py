#Ejercicio 1
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

print(f"Hola {nombre}, Bienvenido")
print(f"Tu edad es: {edad} años")
print("---------------------------------------")

#Ejercicio 2
n1 = float(input("Introduce un número: "))
n2 = float(input("Introduce otro número: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2

if n2 != 0:
    division = n1 / n2
    print(f"La división de los números es: {division:.2f}")
else:
    print("No se puede dividir por cero.")

print(f"La suma de los números es: {suma:.2f}")
print(f"La resta de los números es: {resta:.2f}")
print(f"La multiplicación de los números es: {multiplicacion:.2f}")
print("---------------------------------------")

#Ejercicio 3
frase = input("Introduce una frase: ")

print(f"En minúsculas: {frase.lower()}")
print(f"En mayúsculas: {frase.upper()}")
print(f"Con cada palabra en mayúscula: {frase.title()}")
print("---------------------------------------")


#Ejercicio 4
from datetime import datetime

def calcular_dias_desde_nacimiento():
    fecha_nacimiento_str = input("Introduce tu fecha de nacimiento en formato DD/MM/AAAA: ")
    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        fecha_actual = datetime.now()
        diferencia_dias = (fecha_actual - fecha_nacimiento).days
        print(f"Han pasado {diferencia_dias} días desde tu fecha de nacimiento.")
    except ValueError:
        print("Formato de fecha inválido. Usa DD/MM/AAAA.")

calcular_dias_desde_nacimiento()
print("---------------------------------------")


#Ejercicio 5
def redondear_a_dos_decimales():
    try:
        numero = float(input("Introduce un número flotante: "))
        numero_redondeado = round(numero, 2)
        print(f"El número redondeado a dos decimales es: {numero_redondeado}")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número flotante.")

redondear_a_dos_decimales()
print("---------------------------------------")


#Ejercicio 6
def mostrar_contenido_archivo():
    nombre_archivo = input("Introduce el nombre del archivo de texto (con extensión): ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("Archivo no encontrado. Verifica el nombre y la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

mostrar_contenido_archivo()
print("---------------------------------------")


#Ejercicio 7
def sumar_numeros():
    numeros = input("Introduce una lista de números separados por comas: ")
    try:
        lista_numeros = [float(num) for num in numeros.split(',')]
        suma = sum(lista_numeros)
        print(f"La suma de los números es: {suma}")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")

sumar_numeros()
print("---------------------------------------")


#Ejercicio 8
cadena_1 = input("Introduce tu cadena: ")
cadena_2 = input("Introduce tu otra cadena: ")

print(f"{cadena_1} {cadena_2}")
print("---------------------------------------")


#Ejercicio 9
tu_nombre = input("Introduce tu nombre: ")
tu_nombre_invertido = tu_nombre[::-1]
print(f"Tu nombre invertido: {tu_nombre_invertido}")
print("---------------------------------------")


#Ejercicio 10
def calcular_promedio_calificaciones():
    try:
        num_calif = int(input("Ingrese el número de calificaciones a registrar: "))
        if num_calif <= 0:
            print("El número de calificaciones debe ser mayor a 0.")
            return

        lista_calificaciones = []
        for _ in range(num_calif):
            calif = float(input("Ingrese la calificación: "))
            lista_calificaciones.append(calif)

        promedio = sum(lista_calificaciones) / len(lista_calificaciones)
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números válidos.")

calcular_promedio_calificaciones()
print("---------------------------------------")


#Ejercicio 11
try:
    peso = float(input("Introduce tu peso en kilogramos: "))
    altura = float(input("Introduce tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal es: {imc:.2f}")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números válidos.")
print("---------------------------------------")


#Ejercicio 12
import random

numero = random.randint(1, 100)
print("ADIVINA EL NÚMERO")

while True:
    try:
        numero_usuario = int(input("Ingresa un número: "))
        if numero_usuario == numero:
            print("¡Felicidades, adivinaste el número!")
            break
        elif numero_usuario < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
print("---------------------------------------")
 

#Ejercicio 13
def ordenar_nombres():
    try:
        cantidad = int(input("¿Cuántos nombres deseas ingresar? "))
        nombres = [input(f"Introduce el nombre {i + 1}: ") for i in range(cantidad)]
        nombres.sort()
        print("Nombres ordenados alfabéticamente:")
        print("\n".join(nombres))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

ordenar_nombres()
print("---------------------------------------")


#Ejercicio 14
try:
    tabla_de_mult = int(input("Introduce cuál tabla de multiplicar quieres: "))
    for i in range(1, 11):
        print(f"{tabla_de_mult} x {i} = {tabla_de_mult * i}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")


#Ejercicio 15
oracion = input("Introduce tu oración: ")
palabras = oracion.split()
print(f"El número de palabras en la oración es: {len(palabras)}")
print("---------------------------------------")
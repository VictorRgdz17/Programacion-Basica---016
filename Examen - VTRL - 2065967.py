'''Problema 4'''
# Definición de las variables
a = 3
b = 4

# Suma las variables
suma1 = a + b

# Imprime el resultado
print("La suma de a y b es:", suma1)
'''Problema 5'''
# Pide el ingreso de un numero
c = int(input("Ingresa un número: "))

# Inicia la variable
resultado2 = 0

# Verifica si es par o impar
if c % 2 == 0:
    resultado2 = c * 2
else:
    resultado2 = c * 3

# Imprimie el resultado
print("El resultado es:", resultado2)
'''Problema 6'''
# Define la función multiplicar
def multiplicar(x, y):
    return x * y

# Usa a función 5 y 6
resultado3 = multiplicar(5, 6)

# Imprime el resultado
print("El resultado de la multiplicación es:", resultado3)
'''Problema 7'''
# Inicia la variable
resultado4 = 0

# Ciclo for 
for i in range(1, 6):
    resultado4 += i  # Sumar el número actual a resultado4

# Imprime la suma
print("La suma total es:", resultado4)
'''Problema 8'''
# Creacion de la lista
numeros = [1, 2, 3, 4, 5]

# Inicia la lista
resultado5 = []

# Multiplicar cada numero por 2
for numero in numeros:
    resultado5.append(numero * 2)

# Imprime la lista
print("La lista resultado5 es:", resultado5)
'''Problema 9'''
# Pide al usuario que ingrese un numero
d = float(input("Ingresa un número para dividir 10: "))

# Inicia la variable
resultado6 = None

# Verifica si d es cero
if d == 0:
    print("Error: división por cero no permitida.")
else:
    # Realiza la división
    resultado6 = 10 / d
    # Imprime el resultado
    print("El resultado de la división es:", resultado6)
'''Problema 10'''
# Define a la persona
persona = {
    "nombre": "Ana",
    "edad": 25,
    "profesión": "Ingeniera"
}

# Accede al diccionario de la persona
resultado7 = persona["edad"]

# Imprime el resultado
print("La edad de la persona es:", resultado7)
'''Problema 11'''
# Pide al usuario que ingrese cualquier oracion
cadena = input("Ingresa una cadena de texto: ")

# Convierte la cadena en mayusculas
cadena_mayusculas = cadena.upper()

# Almacena la cadena
resultado8 = len(cadena_mayusculas)

# Imprime la cadena en mayusculas
print("La longitud de la cadena en mayúsculas es:", resultado8)
'''Problema 12'''
# Define la función y la calcula al cuadrado
cuadrado = lambda x: x ** 2

# Aplica la función 7
resultado9 = cuadrado(7)

# Imprime el resultado
print("El cuadrado de 7 es:", resultado9)
'''Problema 13'''
# Crea una lista de numero pares entre 1y 10
numeros_pares = [x for x in range(1, 11) if x % 2 == 0]

# Calcula la suma
resultado10 = sum(numeros_pares)

# Imprime el resultado
print("La suma de los números pares entre 1 y 10 es:", resultado10)
# Combinando los resultados
total = suma1 + resultado2 + resultado3 + resultado4 + sum(resultado5) + resultado6 + resultado7 + resultado8 + resultado9 + resultado10
print("El resultado final es:", total)
#Ejemplo 1
def max_in_list(numbers):
    # Verifica si la lista está vacía
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    # Inicializa el valor máximo con el primer elemento de la lista
    max_value = numbers[0]
    
    # Recorre la lista comenzando desde el segundo elemento
    for num in numbers[1:]:
        # Actualiza el valor máximo si el número actual es mayor
        if num > max_value:
            max_value = num
    
    return max_value
numeros = [39, 54, 78, 29, 47, 23]
print(max_in_list(numeros))

#Ejemplo 2
def mas_larga(palabras):
    if not palabras:
        raise ValueError("La lista no debe estar vacía")
    palabra_larga = palabras[0]
    for palabra in palabras[1:]:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    return palabra_larga
lista_palabras = ["kiraz", "Nazli", "Eda", "Betul"]
print(mas_larga(lista_palabras))

#Ejemplo 3
def filtrar_palabras(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]
lista_palabras = ["Tormenta", "Ventisca", "Arena", "Desierto", "Incendio"]
n = 5
print(filtrar_palabras(lista_palabras, n))

#Ejemplo 4
def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador
cadena_usuario = input("Por favor, ingresa una oracion: ")
num_mayusculas = contar_mayusculas(cadena_usuario)
print(f"La oracion ingresada tiene {num_mayusculas} letras mayúsculas.")

#Ejemplo 5
def binario_a_entero(binario):
    return int(binario, 2)
binario_usuario = input("Por favor, ingresa un número binario: ")
numero_entero = binario_a_entero(binario_usuario)
print(f"El número entero correspondiente es: {numero_entero}")

#Ejemplo 6
def calcular_edad(anio_curso, anio_nacimiento):
    return anio_curso - anio_nacimiento
def main():
    anio_curso = int(input("Ingrese el año en curso: "))
    personas = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
        edad = calcular_edad(anio_curso, anio_nacimiento)
        personas.append((nombre, edad))
    print("\nEdades durante el año en curso:")
    for nombre, edad in personas:
        print(f"{nombre} cumplirá {edad} años.")
if __name__ == "__main__":
    main()

#Ejemplo 7
def contar_mayores_de_20(edades):
    return sum(1 for edad in edades if edad > 20)

def main():
    edades = []
    print("Ingrese 10 edades:")
    for i in range(10):
        while True:
            try:
                edad = int(input(f"Edad {i+1}: "))
                edades.append(edad)
                break
            except ValueError:
                print("Por favor, ingrese un número entero.")
    edades_tupla = tuple(edades)
    cantidad_mayores = contar_mayores_de_20(edades_tupla)
    print(f"Cantidad de personas con edades superiores a 20: {cantidad_mayores}")
if __name__ == "__main__":
    main()

#Ejemplo 8
def contar_nombres_por_letra(nombres, letra):
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))
nombres = ["Ana", "Pedro", "Antonio", "Laura", "Alberto", "María", "Andrés", "Carlos", "Alicia", "Beatriz"]
letra_buscada = 'a'
cantidad = contar_nombres_por_letra(nombres, letra_buscada)
print(f"Cantidad de nombres que comienzan con la letra '{letra_buscada}': {cantidad}")

#Ejemplo 9
def contar_vocales(palabra):
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    palabra = palabra.lower()
    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
    return conteo_vocales
def main():
    palabra_usuario = input("Ingrese una palabra: ")
    conteo = contar_vocales(palabra_usuario)
    print("Conteo de vocales:")
    for vocal, cantidad in conteo.items():
        print(f"Vocal '{vocal}': {cantidad} veces")
if __name__ == "__main__":
    main()

#Ejemplo 10
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
anio = int(input("Ingrese un año: "))
if es_bisiesto(anio):
    print(f"El año {anio} es un año bisiesto.")
else:
    print(f"El año {anio} no es un año bisiesto.")

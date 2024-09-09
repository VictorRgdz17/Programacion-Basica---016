'''Actividades de Recursividad'''
#Actividad 1
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)
numero = 5
print(f"El factorial de {numero} es {factorial(numero)}")

#Actividad 2
def fibonacci(n):
    # Caso base: el primer y segundo número de Fibonacci son 0 y 1, respectivamente
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
numero = 6
print(f"El {numero}° número de Fibonacci es {fibonacci(numero)}")

#Actividad 3
def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter
    if len(cadena) == 0:
        return ""
    # Caso recursivo: toma el último carácter y lo concatena con la inversión del resto de la cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
texto = "hola"
print(f"La cadena invertida de '{texto}' es '{invertir_cadena(texto)}'")

#Actividad 4
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: a^b = a * a^(b-1)
    else:
        return base * potencia(base, exponente - 1)
a = 2
b = 3
print(f"{a} elevado a {b} es {potencia(a, b)}")

#Actividad 5
def suma_digitos(n):
    # Caso base: si n es 0, la suma de los dígitos es 0
    if n == 0:
        return 0
    # Caso recursivo: suma el último dígito y llama a la función con el número sin ese dígito
    else:
        return n % 10 + suma_digitos(n // 10)
numero = 1234
print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")

'''Actividades de Divide y Venceras'''
#Actividad 6
def merge_sort(arr):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Ordenar la mitad izquierda
    right_half = merge_sort(arr[mid:])  # Ordenar la mitad derecha

    # Mezclar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Mezclar las dos listas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Añadir los elementos restantes de left (si hay)
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # Añadir los elementos restantes de right (si hay)
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista ordenada: {merge_sort(lista)}")

#Actividad 7
def quick_sort(arr):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Elegir un pivote (en este caso, el último elemento)
    pivot = arr[-1]
    left = []  # Elementos menores que el pivote
    right = []  # Elementos mayores que el pivote
    equal = []  # Elementos iguales al pivote

    # Dividir la lista en sublistas
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            equal.append(item)

    # Recursivamente aplicar quick_sort a las sublistas
    return quick_sort(left) + equal + quick_sort(right)
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista ordenada: {quick_sort(lista)}")

#Actividad 8
def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
    # Inicializar el valor de derecha en la primera llamada
    if derecha is None:
        derecha = len(lista) - 1
    
    # Caso base: si el rango es inválido, el objetivo no está en la lista
    if izquierda > derecha:
        return -1  # Retorna -1 si no se encuentra el objetivo

    # Calcular el punto medio
    medio = (izquierda + derecha) // 2
    
    # Comparar el elemento medio con el objetivo
    if lista[medio] == objetivo:
        return medio  # Retorna la posición del objetivo
    elif lista[medio] < objetivo:
        # Buscar en la mitad derecha
        return busqueda_binaria(lista, objetivo, medio + 1, derecha)
    else:
        # Buscar en la mitad izquierda
        return busqueda_binaria(lista, objetivo, izquierda, medio - 1)
lista = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 7
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El objetivo {objetivo} no se encuentra en la lista.")

#Actividad 9
def multiplicar_matrices(A, B):
    # Obtiene el tamaño de las matrices
    n = len(A)

    # Caso base: si la matriz es 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]

    # Divide las matrices en cuadrantes
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    # Realiza las multiplicaciones recursivas
    C11 = sumar_matrices(multiplicar_matrices(A11, B11), multiplicar_matrices(A12, B21))
    C12 = sumar_matrices(multiplicar_matrices(A11, B12), multiplicar_matrices(A12, B22))
    C21 = sumar_matrices(multiplicar_matrices(A21, B11), multiplicar_matrices(A22, B21))
    C22 = sumar_matrices(multiplicar_matrices(A21, B12), multiplicar_matrices(A22, B22))

    # Combina los cuadrantes en la matriz resultante
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

def sumar_matrices(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(A, B)

print("Resultado de la multiplicación de matrices:")
for fila in resultado:
    print(fila)

#Actividad 10
def multiplicar_matrices(A, B):
    n = len(A)
    # Inicializa la matriz resultante con ceros
    C = [[0] * n for _ in range(n)]
    
    # Multiplica las matrices A y B
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def potencia_matriz(matriz, exponente):
    n = len(matriz)
    # Caso base: cualquier matriz elevada a la potencia 0 es la matriz identidad
    if exponente == 0:
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    # Caso base: la matriz elevada a la potencia 1 es la misma matriz
    elif exponente == 1:
        return matriz
    
    # Divide y conquista
    half_pow = potencia_matriz(matriz, exponente // 2)
    
    if exponente % 2 == 0:
        # Si el exponente es par
        return multiplicar_matrices(half_pow, half_pow)
    else:
        # Si el exponente es impar
        return multiplicar_matrices(matriz, multiplicar_matrices(half_pow, half_pow))
matriz = [[1, 2], [3, 4]]
exponente = 3
resultado = potencia_matriz(matriz, exponente)

print(f"La matriz elevada a la potencia {exponente} es:")
for fila in resultado:
    print(fila)
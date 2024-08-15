def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print(superposicion([1, 2, 3], [3, 4, 5]))
print(superposicion([1, 2, 3], [4, 5, 6]))
print(superposicion([], [1, 2, 3]))
print(superposicion([1, 2, 3], []))
print(superposicion([1, 2, 3], [2]))

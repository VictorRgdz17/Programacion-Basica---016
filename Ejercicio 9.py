def generar_n_caracteres(n, caracter):
    if len(caracter) != 1:
        raise ValueError("El segundo argumento debe ser un carácter único.")
    return caracter * n
print(generar_n_caracteres(5, "x"))
print(generar_n_caracteres(3, "#"))
print(generar_n_caracteres(0, "a"))

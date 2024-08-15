def es_palindromo(cadena):
    cadena_limpia = cadena.replace(" ", "").lower()
    cadena_invertida = cadena_limpia[::-1]
    return cadena_limpia == cadena_invertida
print(es_palindromo("radar"))
print(es_palindromo("hola"))
print(es_palindromo("A man a plan a canal Panama"))

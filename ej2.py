# Lista de enteros
lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Potencia n
n = 3

# Calcular la potencia n-ésima de cada elemento en la lista usando lambda
resultado = list(map(lambda x: x ** n, lista_enteros))

# Mostrar el resultado
print(resultado)

# Matriz X
X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

# Calcular la matriz transpuesta XT usando lambda
XT = list(map(lambda *row: list(row), *X))

# Mostrar el resultado
for row in XT:
    print(row)

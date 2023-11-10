# Matriz X
X = [ 
    [1],
    [2],
    [3]
]

# Calcular la matriz transpuesta XT usando lambda
XT = list(map(lambda *row: list(row), *X))

# Mostrar el resultado
for row in XT:
    print(row)

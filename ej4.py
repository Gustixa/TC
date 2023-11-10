# Lista inicial
lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
print(f"lista original: {lista_inicial}")
# Lista de elementos a borrar
elementos_a_borrar = ['amarillo', 'café', 'blanco']
print(f"Elementos a eliminar: {elementos_a_borrar}")
# Eliminar elementos indicados usando lambda
lista_resultante = list(filter(lambda x: x not in elementos_a_borrar, lista_inicial))

# Mostrar el resultado
print(f"Lista resultante: {lista_resultante}")

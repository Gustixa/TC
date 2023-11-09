# Lista original de diccionarios
D = [{'make':'Nokia', 'model':'216', 'color':'Black'},
     {'make':'Apple', 'model':'2', 'color':'Silver'},
     {'make':'Huawei', 'model':'50', 'color':'Gold'},
     {'make':'Samsung', 'model':'7','color':'Blue'}]

# Clave para ordenar la lista de diccionarios
key_to_sort = 'model'

# Función lambda para obtener el valor de la clave, manejando enteros y cadenas
get_value = lambda x: int(x[key_to_sort]) if key_to_sort == 'model' else x[key_to_sort]

# Ordenar la lista de diccionarios por la clave indicada
sorted_D = sorted(D, key=get_value)

# Mostrar la lista ordenada
print(sorted_D)

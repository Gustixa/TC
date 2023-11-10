# Lista original de diccionarios
'''
D = [{'make':'Nokia', 'model':'216', 'color':'Black'},
     {'make':'Apple', 'model':'2', 'color':'Silver'},
     {'make':'Huawei', 'model':'50', 'color':'Gold'},
     {'make':'Samsung', 'model':'7','color':'Blue'}]
'''
D = [{'product':'Laptop', 'price':'1000', 'color':'Silver'},
     {'product':'Smartphone', 'price':'800', 'color':'Black'},
     {'product':'Tablet', 'price':'500', 'color':'Gold'}]

# Clave para ordenar la lista de diccionarios
key_to_sort = 'price'

# Función lambda para obtener el valor de la clave, manejando enteros y cadenas
get_value = lambda x: int(x[key_to_sort]) if key_to_sort == 'price' else x[key_to_sort]

# Ordenar la lista de diccionarios por la clave indicada
sorted_D = sorted(D, key=get_value)

# Mostrar la lista ordenada
print(sorted_D)

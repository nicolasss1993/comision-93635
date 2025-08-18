lista = []
lsita_1 = list()

lista_nro = [1, 2, 3, "Hola", [], "mundo"]
#            0  1  2    3     4     5

# print(lista_nro[3]) # Slicing (inicio: Fin : Salto)
# print(lista_nro[0:4])

lista_slicing = lista_nro[::-2] # Crea una lista nueva y ocupa mas memoria.
# print(lista_slicing)

# Agregar datos a una lista #

lista_nro.append(45) # Agrega el elemento en la ultima posicion.
lista_nro.insert(0, "Nicolas") # (Indice, Elemento a agregar)
lista_nro.extend([888, "Otra cadena", "Nicolas"]) # Esto agrega elementos a la lista ya existente.
#lista_nro_2 = lista_nro + [87, "Hola que tal"] # Este crea una lista nueva con la suma de las anteriores.
# print(lista_nro)
# Eliminar datos de una lista #
# lista_nro.remove("Nicolas") # Elimina la primera aparicion del elemento que le paso.
# elemento_eliminado = lista_nro.pop()
# lista_nro.clear() # Vacia la lista
# lista_nro = lista_nro[:len(lista_nro)-1]
# print(lista_nro.index("Hola")) # me devuelve le indice del elemento que le paso.
# print(lista_nro.count("Nicolas")) # Cuenta las apareciones del elemento que le paso.

lista_numero = [1, 2 , 5, 3, 10, 8]
lista_numero.sort() # Ordena de menor a mayor. key=funcion de ordenamiento, reverse=False
lista_numero.reverse() # Da vuelta la lista, esto es lo mismo que hacer lista_numero[::-1]
# print(lista_numero)

#lista_copia_numero = lista_numero.copy() Copia la lista donde se llame .copy
# print(lista_numero.copy(), lista_numero)

# print(len(lista_numero))
# print(sum(lista_numero))
# print(max(lista_numero))
# print(min(lista_numero))
# -------------------------------------------------------

tuplas = ()
tuplas_1 = tuple()

tuple_nro = (1, 2, 3)
# print(tuple_nro[0:2])

lista_tupla_nro = list(tuple_nro)
# print(lista_tupla_nro)
# print(tuple(lista_tupla_nro))

# ---------------------------------------------------------

conjuntos = set() # {}
conjuntos_1 = {1, 10, 4}
conjuntos_2 = set([1, 1, 5, 5 , 6])
# print(conjuntos_2)
# conjuntos_2.add(510)
# print(conjuntos_2)
# #conjuntos_2.remove(10)
# #conjuntos_2.discard(1)
# print(conjuntos_2)

# print( 51 in conjuntos_2)
# print(len(conjuntos_2))

# print(conjuntos_2 | conjuntos_1) # Union
# print(conjuntos_2 & conjuntos_1) # Intersecion

# conjuntos_2.update([70, 51, 1, 510])
# conjuntos_2.clear()
# print(conjuntos_2)

# --------------------------------------------------------------------
"clave: valor" # la clave tiene que ser un int o str, float
diccionario = {}
diccionario = dict()

diccionario = {
    "nombre": "Nicolas",
    "apellido": "Dziuma",
    "edad": 30
}
diccionario_usuarios = {
    "usuarios": [
        {
            "usuario": "nicolas123",
            "password": "admin123"
        },
        {
            "usuario": "fede54",
            "password": "admin12"
        },
    ]
}
diccionario_usuarios["usuarios"][0]["usuario"] = "azul5875"
print(diccionario_usuarios["usuarios"][0]["usuario"])
diccionario_1 = dict(nombre=["Nicolas"], apellido="Dziuma", edad=30)
print(diccionario_1, diccionario)
print(diccionario["nombre"])
print(diccionario.get("nombree", [])) # Me devuelve el valor de la key que le paso como primer parametro.
# var = None # null
# dict_values = list(diccionario.values())
# dict_values.append(50)
# print(dict_values)
print(diccionario.keys()) # Devuelve todas las claves
print(diccionario.values()) # Devuelve todos los valores del dict
print(diccionario.items()) # Devuelve todas las clave, valor en una lista de tuplas [(clave, valor)... ()]

# var_eliminada = diccionario.pop("nombre")
# print(var_eliminada)
print("nombre" in diccionario)
diccionario.update({"Domicilio": "Calle False 123"})
diccionario["telefono"] = "111111111"
diccionario["telefono"] = "222222222"
#diccionario.clear()
ultimo = diccionario.popitem() # Devuelve el ultimo elemento en la lista con formato (clave, valor)
print(ultimo)
# Listas en Python - Resumen y ejemplos

# ---------------------------------------------------
# Características principales de las listas en Python
# ---------------------------------------------------
# - Colección ordenada y mutable (se pueden modificar).
# - Se definen con corchetes [] .
# - Pueden contener distintos tipos de datos.
# - Se accede a sus elementos mediante índices (desde 0).
# - Son mutables: se pueden agregar, eliminar y cambiar elementos.

mi_lista = [10, "hola", 3.14, True]
print(mi_lista[1])   # "hola"

# ---------------------------------------------------
# Métodos más usados en listas
# ---------------------------------------------------

ejemplo = [1, 2, 3]

ejemplo.append(4)         # Agrega al final
print("append:", ejemplo)

ejemplo.insert(1, 99)     # Inserta en posición 1
print("insert:", ejemplo)

ejemplo.extend([5, 6])    # Extiende con otra lista
print("extend:", ejemplo)

ejemplo.remove(99)        # Elimina la primera ocurrencia de 99
print("remove:", ejemplo)

ejemplo.pop()             # Elimina el último elemento
print("pop:", ejemplo)

print("index de 2:", ejemplo.index(2))  # Devuelve índice de la primera ocurrencia de 2
print("count de 3:", ejemplo.count(3))  # Cuenta cuántas veces aparece 3

ejemplo.sort()            # Ordena la lista (key=None, reverse=False)
print("sort:", ejemplo)

ejemplo.reverse()         # Invierte el orden
print("reverse:", ejemplo)

copia = ejemplo.copy()    # Crea una copia
print("copy:", copia)

# ---------------------------------------------------
# Otras operaciones útiles
# ---------------------------------------------------

lista1 = [1, 2, 3]
lista2 = [4, 5]

# Concatenación crea una lista nueva
lista3 = lista1 + lista2
print("Concatenación (+):", lista3)
print("Lista1 no se modifica:", lista1)

# extend modifica la lista original
lista1.extend(lista2)
print("Usando extend:", lista1)

# Repetición
print("Repetición:", [0] * 5)

# Slices (rebanadas)
numeros = [10, 20, 30, 40, 50]
print("Slice 1:4:", numeros[1:4])
print("Slice :3:", numeros[:3])
print("Slice ::2:", numeros[::2])

# ---------------------------------------------------
# Diferencia entre concatenación y extend (con id)
# ---------------------------------------------------

lista_a = [2, 3]
lista_b = [1]

resultado = lista_a + lista_b
print("\nConcatenación con +:")
print("Resultado:", resultado)
print("lista_a sigue igual:", lista_a)
print("id(lista_a):", id(lista_a))

lista_a.extend(lista_b)
print("\nUsando extend:")
print("lista_a modificado:", lista_a)
print("id(lista_a) después de extend:", id(lista_a))

# ---------------------------------------------------
# Mini ejercicio: Lista de compras
# ---------------------------------------------------

lista_compras = []
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")

print("\nLista de compras inicial:", lista_compras)

lista_compras.remove("Pan")
print("Después de eliminar 'Pan':", lista_compras)

lista_compras.sort()
print("Ordenada:", lista_compras)

lista_compras.reverse()
print("Reversa:", lista_compras)

#---------------------------------------------------
# Funciones para listas
#---------------------------------------------------

numeros = [5, 2, 9, 1]

print("Cantidad de elementos:", len(numeros))   # 4
print("Suma total:", sum(numeros))             # 17
print("Mayor:", max(numeros))                  # 9
print("Menor:", min(numeros))                  # 1
print("Ordenada:", sorted(numeros))            # [1, 2, 5, 9]
print("Invertida:", list(reversed(numeros)))   # [1, 9, 2, 5]

# any y all
print(any([0, False, 3]))   # True (porque hay un 3 que es "verdadero")
print(all([1, 2, 3]))       # True (todos son verdaderos)

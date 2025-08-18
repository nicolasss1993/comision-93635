# ==========================
# RESUMEN SOBRE TUPLAS
# ==========================

# Una TUPLA es una colección ordenada e inmutable.
# Esto significa:
# - Mantiene el orden en que se definen los elementos.
# - No se pueden modificar (agregar, eliminar o cambiar) después de crearse.
# - Se usan normalmente para agrupar datos fijos.
# - Se definen con () en vez de [].

# --------------------------
# Crear tuplas
# --------------------------
tupla1 = (1, 2, 3, 4)
tupla2 = ("a", "b", "c")
tupla_mixta = (1, "hola", 3.5, True)

# Una tupla con un solo elemento necesita la coma final:
tupla_un_elemento = (5,)

print("Tupla 1:", tupla1)
print("Tupla mixta:", tupla_mixta)
print("Tupla un elemento:", tupla_un_elemento)


# --------------------------
# Indexación y slicing
# --------------------------
print("\n--- Indexación y slicing ---")
print("Primer elemento:", tupla1[0])       # 1
print("Último elemento:", tupla1[-1])      # 4
print("Slice del 1 al 3:", tupla1[1:3])    # (2, 3)


# --------------------------
# Funciones integradas con tuplas
# --------------------------
print("\n--- Funciones integradas ---")
print("Longitud de tupla1:", len(tupla1))
print("Suma de tupla1:", sum(tupla1))
print("Máximo de tupla1:", max(tupla1))
print("Mínimo de tupla1:", min(tupla1))

# Funciona también con strings en una tupla:
print("Máximo de tupla2:", max(tupla2))   # 'c'
print("Mínimo de tupla2:", min(tupla2))   # 'a'


# --------------------------
# Métodos de tuplas
# --------------------------
# Aunque son inmutables, tienen algunos métodos útiles:

print("\n--- Métodos ---")
tupla3 = (1, 2, 3, 2, 4, 2)

print("Cantidad de veces que aparece 2:", tupla3.count(2))   # 3
print("Índice de la primera aparición de 3:", tupla3.index(3)) # 2

# Métodos con parámetros extra:
# index(valor, inicio, fin) -> busca dentro de un rango
print("Índice de 2 entre posición 2 y 5:", tupla3.index(2, 2, 5))  # 3


# --------------------------
# Conversión a lista
# --------------------------
# Si necesitas modificar una tupla, puedes convertirla a lista.
print("\n--- Conversión a lista ---")
lista_desde_tupla = list(tupla1)
print("Lista convertida:", lista_desde_tupla)

# Y al revés: convertir lista a tupla
print("Tupla convertida:", tuple(lista_desde_tupla))

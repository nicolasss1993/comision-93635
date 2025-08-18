# ==========================
# RESUMEN SOBRE DICCIONARIOS
# ==========================

# Un DICCIONARIO es una colección de pares **clave: valor**.
# Características:
# - Las claves son únicas e inmutables (números, strings, tuplas).
# - Los valores pueden ser de cualquier tipo.
# - Es **mutable**: se puede agregar, modificar o eliminar elementos.
# - No mantiene un orden fijo antes de Python 3.7; desde 3.7 mantiene el orden de inserción.

# --------------------------
# Crear diccionarios
# --------------------------
diccionario1 = {"nombre": "Ana", "edad": 25, "ciudad": "Buenos Aires"}
diccionario2 = dict(a=1, b=2, c=3)
diccionario_vacio = {}

print("Diccionario 1:", diccionario1)
print("Diccionario 2:", diccionario2)

# --------------------------
# Acceder y modificar elementos
# --------------------------
print("\n--- Acceder y modificar ---")
print(diccionario1["nombre"])      # Ana
diccionario1["edad"] = 26          # modificar valor
diccionario1["profesion"] = "Ing"  # agregar nueva clave
print("Actualizado:", diccionario1)

# --------------------------
# Métodos de diccionarios
# --------------------------
print("\n--- Métodos ---")
print("Claves:", diccionario1.keys())        # dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])
print("Valores:", diccionario1.values())    # dict_values(['Ana', 26, 'Buenos Aires', 'Ing'])
print("Items:", diccionario1.items())       # dict_items([('nombre', 'Ana'), ('edad', 26), ...])

# get() -> devuelve valor si la clave existe, sino un valor por defecto
print("Obtener edad:", diccionario1.get("edad"))      # 26
print("Obtener pais:", diccionario1.get("pais", "No definido"))  # No definido

# pop() -> elimina y devuelve el valor de una clave
valor = diccionario1.pop("profesion")
print("Valor eliminado:", valor)
print("Diccionario actual:", diccionario1)

# popitem() -> elimina y devuelve el último par clave-valor agregado
ultimo = diccionario1.popitem()
print("Último par eliminado:", ultimo)
print("Diccionario ahora:", diccionario1)

# update() -> agrega o actualiza pares clave-valor
diccionario1.update({"pais": "Argentina", "edad": 27})
print("Después de update:", diccionario1)

# clear() -> elimina todos los elementos
diccionario2.clear()
print("Diccionario2 vacío:", diccionario2)

# --------------------------
# Funciones integradas con diccionarios
# --------------------------
print("\n--- Funciones integradas ---")
dic = {"a": 10, "b": 20, "c": 30}

print("len(dic):", len(dic))  # cantidad de pares
print("max(dic):", max(dic))  # devuelve la clave máxima según orden
print("min(dic):", min(dic))  # devuelve la clave mínima
print("sum(dic.values()):", sum(dic.values()))  # suma de los valores
print("any(dic.values()):", any(dic.values()))  # True si algún valor es True
print("all(dic.values()):", all(dic.values()))  # True si todos los valores son True

# ------------------------------------------------------------------------------------------
"""Reglas para las claves

. Deben ser inmutables: no se puede usar algo que pueda cambiar, como listas o diccionarios.
. Deben ser únicas: no puede haber dos claves iguales; si se repite, se sobrescribe el valor.
. Cualquier tipo hashable funciona, por ejemplo:
-    int → 1, 42

-    float → 3.14

-    str → "hola"

-    tuple → (1,2) (si los elementos dentro también son inmutables)

-    bool → True / False
"""
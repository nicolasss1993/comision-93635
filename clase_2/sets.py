# ==========================
# RESUMEN SOBRE CONJUNTOS (SETS)
# ==========================

# Un CONJUNTO es una colección **desordenada y sin elementos repetidos**.
# Características:
# - No mantiene orden (no se accede por índice).
# - No permite duplicados.
# - Es mutable (podés agregar o eliminar elementos).
# - Se define con llaves {} o con set() si está vacío.

# --------------------------
# Crear conjuntos
# --------------------------
conjunto1 = {1, 2, 3, 4}
conjunto2 = set([3, 4, 5, 6])
conjunto_vacio = set()  # No se puede usar {} porque sería un dict vacío

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("Conjunto vacío:", conjunto_vacio)

# --------------------------
# Operaciones básicas
# --------------------------
print("\n--- Operaciones básicas ---")
# Agregar elementos
conjunto1.add(5)
print("Agregado 5:", conjunto1)

# Eliminar elementos
conjunto1.remove(2)   # lanza error si no existe
conjunto1.discard(10) # no lanza error si no existe
print("Después de eliminar:", conjunto1)

# Verificar pertenencia
print("3 está en conjunto1?", 3 in conjunto1)
print("2 está en conjunto1?", 2 in conjunto1)

# Longitud
print("Cantidad de elementos:", len(conjunto1))

# --------------------------
# Operaciones de conjuntos (matemáticas)
# --------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\n--- Operaciones de conjuntos ---")
print("Unión (A | B):", A | B)           # {1,2,3,4,5,6}
print("Intersección (A & B):", A & B)    # {3,4}
print("Diferencia (A - B):", A - B)      # {1,2}
print("Diferencia simétrica (A ^ B):", A ^ B)  # {1,2,5,6}

# --------------------------
# Métodos específicos de sets
# --------------------------
print("\n--- Métodos de sets ---")
conjunto3 = {1, 2, 3}
conjunto3.update([3, 4, 5])  # agrega varios elementos
print("update:", conjunto3)

print("pop:", conjunto3.pop())  # elimina y devuelve un elemento arbitrario
conjunto3.clear()               # elimina todos los elementos
print("Después de clear:", conjunto3)

# --------------------------
# Funciones integradas
# --------------------------
print("\n--- Funciones integradas ---")
numeros = {10, 20, 30, 40}

print("len:", len(numeros))
print("max:", max(numeros))
print("min:", min(numeros))
print("sum:", sum(numeros))
print("any:", any(numeros))  # True si algún elemento es True
print("all:", all(numeros))  # True si todos son True

#--------------------------------------------------------------
# No tienen índices, no se puede hacer conjunto[0].

# Útiles para eliminar duplicados y operaciones matemáticas como unión, intersección y diferencia.

# Mutables, pero los elementos deben ser inmutables (números, strings, tuplas, etc.).

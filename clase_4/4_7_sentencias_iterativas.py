"""
4.4 Sentencias Iterativas en Python

Este archivo contiene explicaciones y ejemplos de cómo utilizar las sentencias iterativas en Python,
con un enfoque en la estructura 'while'. También se cubre la estructura 'while-else' y el uso de la 
sentencia 'break' para controlar el flujo de los bucles.

Descripción del archivo
Estructura de un bucle while: Incluye la explicación detallada de cómo funciona la condición y cómo se deben actualizar las variables para evitar bucles infinitos.
Ejemplos adicionales:
Ejemplo de un bucle while simple que cuenta hasta 4.
Ejemplo de control de bucle para evitar ciclos infinitos.
Ejemplo de uso de while-else y cómo break afecta al bloque else.
Ejemplo de sistema de control de acceso con intentos limitados.

"""

# Introducción a las Sentencias Iterativas
print("Introducción a las Sentencias Iterativas en Python")
print("--------------------------------------------------")

# En Python, las sentencias iterativas permiten repetir la ejecución de un bloque de código mientras
# se cumpla una condición específica. La estructura 'while' es una de las más comunes y útiles.

# Introducción a la Sentencia While
print("\nEjemplo Básico de un Bucle While")
print("----------------------------------")

# Sintaxis y flujo de ejecución de 'while':
# La estructura básica de un bucle 'while' en Python es la siguiente:
#
# while condición:
#     # Bloque de código a ejecutar mientras la condición sea verdadera
#
# Condición: Es una expresión que se evalúa antes de cada iteración del bucle. 
# Si es True, el bloque dentro del bucle se ejecuta. Si es False, el bucle termina.

# Ejemplo 1: Bucle 'while' básico
contador = 0
print("Ejemplo 1: Bucle 'while' que cuenta hasta 4")
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Actualiza el contador para evitar un bucle infinito

# # Importancia de Evitar Bucles Infinitos
# print("\nImportancia de Evitar Bucles Infinitos")
# print("----------------------------------------")
# Un bucle infinito ocurre cuando la condición nunca se evalúa como False,
# lo cual puede hacer que el programa se quede en un ciclo interminable.

# Ejemplo 2: Bucle infinito (NO EJECUTAR, solo para referencia)
contador = 0
while contador < 5:
    print(contador)
contador = 0
while True:
    print(contador)
    print(f"Contador: {contador}")
    contador += 1  # Actualiza el contador para evitar un bucle infinito
    # Aquí falta actualizar el contador, el bucle será infinito

# Ejemplo 3: Controlando un bucle con una condición adicional para evitar un ciclo infinito
print("\nEjemplo 3: Bucle controlado con una condición extra para evitar el ciclo infinito")
contador = 0
limite = 500
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 500:  # Evita que el contador se descontrole y cause un bucle infinito
        print("Alerta: posible bucle infinito evitado.")
        break
        # Interrumpe el bucle si el contador es inusualmente alto

# Sentencia While-Else
# print("\nSentencia While-Else")
# print("---------------------")

# La estructura 'while-else' permite ejecutar un bloque adicional cuando el bucle termina de forma 
# natural, es decir, cuando la condición se vuelve False, sin ser interrumpido por un 'break'.

# Ejemplo 4: Uso de 'while-else'
contador = 0
print("Ejemplo 4: Uso de 'while-else'")
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1


# # Uso de 'break' en While-Else
# print("\nUso de 'break' en While-Else")
# print("------------------------------")

# # Si se utiliza 'break' para interrumpir el bucle, el bloque 'else' no se ejecuta.
# # Esto es útil cuando queremos terminar el bucle bajo una condición especial.

# # Ejemplo 5: Interrupción de un 'while' con 'break'
contador = 0
print("Ejemplo 5: Uso de 'break' en un bucle 'while'")
while contador < 5:
    print(f"Contador: {contador}")
    if contador == 2:
        print("Bucle interrumpido con 'break'")
        break  # Rompe el bucle cuando contador es 2
    contador += 1
else:
    print("Este mensaje no se mostrará porque se usó 'break'")

# # Ejemplo adicional: control de acceso a un sistema con intentos limitados
# print("\nEjemplo 6: Intentos limitados en un sistema de control de acceso")
# print("-------------------------------------------------------------------")

# # En este ejemplo, simularemos un sistema de control de acceso con 3 intentos de contraseña.

password_correcto = "abc123"
intentos = 3
print("Introduce la contraseña (tienes 3 intentos):")

while intentos > 0:
    password = input("Contraseña: ")
    if password == password_correcto:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
else:
    print("Acceso denegado. Has agotado todos los intentos.")

# # Conclusión
# print("\nConclusión")
# Las sentencias iterativas como 'while' son esenciales para repetir acciones en un programa mientras
# se cumplan ciertas condiciones. Es fundamental comprender el flujo de ejecución de 'while' y 
# 'while-else', y evitar errores comunes como los bucles infinitos.


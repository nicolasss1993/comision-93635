
# --------------------------------------------------------------
# Creación de Funciones
# --------------------------------------------------------------
def saludar(): # Aca defino la funcion
    """
    Esta función imprime un mensaje de saludo.
    """ # Aca documento la funcion
    print("Hola, ¿cómo estás?") # Aca va el codigo de la funcion

# Llamada a la función
#saludar()
# Salida esperada: Hola, ¿cómo estás?

# --------------------------------------------------------------
# Parámetros y Argumentos
# --------------------------------------------------------------
def saludar_con_nombre(nombre): # Aca nombre es el parametro
    """
    Esta función recibe un nombre como parámetro y saluda a esa persona.
    """
    print(f"Hola, {nombre}, ¿cómo estás?")
    # return None
# # Llamada a la función con un argumento:
# saludar_con_nombre("Juan") # Aca Juan seria el Argumento
# # Salida esperada: Hola, Juan, ¿cómo estás?

# # --------------------------------------------------------------
# # Retorno de Valores
# # --------------------------------------------------------------

def resta(a, b):
    """
    Esta función toma dos números como parámetros y retorna su suma.
    """
    return a - b

# # Llamada a la función y almacenando el resultado:
resultado = resta(5, 3)
print(resultado)
print(resta(15, 10))
# # Salida esperada: 8

# # --------------------------------------------------------------
# # Sintaxis Básica de una Función
# # --------------------------------------------------------------

def multiplicar(a, b):
    """
    Toma dos números y retorna su producto.
    """
    resultado = a * b
    return resultado

# # Llamada a la función:
print(multiplicar(4, 5))
# # Salida esperada: 20

# # --------------------------------------------------------------
# # Ejemplo Práctico
# # --------------------------------------------------------------

def crear_saludo(nombre):
    """
    Recibe un nombre y retorna un mensaje de saludo.
    """
    mensaje = f"Hola, {nombre}!"
    return mensaje

# # Llamada a la función:
resultado = crear_saludo("Ana")
print(resultado)
print(crear_saludo("Luis"))
# # Salida esperada: Hola, Ana!

# # --------------------------------------------------------------
# # Definición y Llamada de una Función
# # --------------------------------------------------------------

# # Definición de una función:
def restar(a, b):
    """
    Resta el segundo parámetro del primero y retorna el resultado.
    a: Es un nro entero
    b: Es un nro entero
    return: La resta de a - b
    """
    return a - b

# # Llamada a la función:
resultado = restar(10, 5)
print(resultado)
# # Salida esperada: 5

# # --------------------------------------------------------------
# # Ejemplo de Función Básica
# # --------------------------------------------------------------

def saludar_simple(): # Definicion de la función
    """
    Imprime un mensaje de saludo.
    """ # Documentacion de la función
    print("Estoy saludando desde la función") # el bloque de codigop de la función

# # Llamada a la función
saludar_simple()
# # Salida esperada: Estoy saludando desde la función

# # --------------------------------------------------------------
# # Ejemplo Completo
# # --------------------------------------------------------------

# # Este ejemplo incluye una función definida y llamada en el código principal.
# def despedirse():
#     """
#     Imprime un mensaje de despedida.
#     """
#     print("Adiós, hasta luego!")

# # Llamada a la función
# despedirse()
# # Salida esperada: Adiós, hasta luego!

# # --------------------------------------------------------------
# # Conclusión
# # --------------------------------------------------------------


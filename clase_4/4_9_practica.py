"""
Explicación de cada sección:
Estructura de Menú: Cada opción en el menú de ejercicio_1 permite realizar una operación matemática específica entre dos números. Incluye validación de entrada para manejar errores.

Validación de Número Impar: ejercicio_2 solicita un número impar y repite el proceso hasta recibir un número correcto.

Suma de Impares: ejercicio_3 usa range para sumar números impares hasta 100 de manera eficiente.

Cálculo de Media: ejercicio_4 permite al usuario especificar cuántos números quiere sumar y calcula su media.

Validación en Lista: ejercicio_5 pide un número entre 0 y 9, verificando si pertenece a una lista del 0 al 9.

Generación de Listas Dinámicas: ejercicio_6 utiliza range y conversión a listas para crear diferentes listas según los parámetros solicitados."""


# 4.9 Actividad práctica

# ¡Instrucciones e iteración!
# Realiza los ejercicios 1, 2, 3, 4, 5 y 6. A continuación están detallados con ejemplos adicionales.

# Ejercicio 1:
# Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# 1. Mostrar una suma de los dos números
# 2. Mostrar una resta de los dos números (el primero menos el segundo)
# 3. Mostrar una multiplicación de los dos números
# 4. Salir del programa
menu = {
    1: "Suma",
    2: "Resta",
    3: "Multiplicacion",
    4: "Fin del programa",
}
# numero_1 = int(input("ingrese primer numero: "))
# numero_2 = int(input("ingrese segundo numero: "))
# while True:
#     # print(f"1. Mostrar una suma de los dos números")
#     # print(f"2. Mostrar una resta de los dos números (el primero menos el segundo)")
#     # print(f"3. Mostrar una multiplicacion de los numeros")
#     # print(f"4. Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará")
#     for opcion, descripcion in menu.items():
#         print(f"{opcion} - Mostra la operacion {descripcion} de los numeros.")
#     opcion = input("INGRESE OPCION: ")
#     if opcion == "1":
#         print(f"suma {numero_1 + numero_2}")
#     elif  opcion == "2":
#         print(f"resta {numero_1 - numero_2}")  
#     elif  opcion == "3":
#         print(f"multiplicacion {numero_1 * numero_2}")    
#     elif opcion == "4":
#         break
#     else:
#         print("opcion novalida")

# while True:
#     numero_uno = int(input("Ingrese un numero: "))
#     numero_dos = int(input("Ingrese un segundo numero: "))
#     opcion = int(input("Ahora selecciona una opción del 1 al 4:\n 1. Mostrar la sumade los dos numeros.\n 2. Mostrar una resta de los dos numeros.\n 3. Mostrar una multiplicación de los dos números.\n 4. Salir del programa. "))
#     if opcion == 1:
#         print(numero_uno + numero_dos)
#     if opcion == 2:
#         if numero_uno > numero_dos:
#             print(numero_uno-numero_dos)
#         else:
#             print(numero_dos-numero_uno)
#     if opcion == 3:
#         print(numero_uno*numero_dos)
#     if opcion == 4:
#         break

# numero_1 = int(input("Ingrese numero 1:"))
# numero_2 = int(input("Ingrese numero 2:"))
# menu = ["Suma", "Resta", "Multiplicacion", "Fin del programa"]
# longitud_menu = len(menu)
# contador = 0
# while contador <= longitud_menu:
#     if contador == 0:
#         print (numero_1 + numero_2)
#         contador +=1
#     if contador == 1:
#         print (numero_1 - numero_2)
#         contador +=1
#     if contador == 2:
#         print (numero_1 * numero_2)
#         contador += 1
#     if contador == 3:
#         print (menu[contador]) 
#         break

menu = {
    1: "Suma",
    2: "Resta",
    3: "Multiplicacion",
    4: "Fin del programa",
}
while True:
    opcion = int(input(f"Seleccionar una de las siguiente opciones: {menu}"))
    if opcion!=4:
        num1 = int(input("Ingrese primer numero"))
        num2 = int(input("Ingrese segundo numero"))
        if opcion==1:
            print(num1+num2)
        elif opcion==2:
            print(num1-num2)
        elif opcion==3:
            print(num1*num2)
    else:
        break



# while True:
#     # for key, value in menu.items():
#     #     print(f"{key}. {value}")
#     print("Menu:")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicacion")
#     print("4. Terminar ejecucion")
#     entrada = input("Ingrese una opcion: ")
#     numero_1 = input("ingrse un numero ")
#     numero_2 = input("ingrse un numero ")
#     # if numero_1.isdigit():
#     #     numero_1 = int(numero_1)
#     #     else:
#     #         print("No ingresaste un numero entero")
#     #         continue
#     if entrada == "1":
#         print(numero_1 + numero_2)
#     elif entrada == "2":
#         print(numero_1 - numero_2)
#     elif entrada == "3":
#         print(numero_1 * numero_2)
#     elif entrada == "4":
#         break


# Ejercicio 2:
# Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.


# Ejercicio 3:
# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100.


#ejercicio_4()
# Escribe un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.


# Ejercicio 5:
# Escribe un programa que pida al usuario un número entero del 0 al 9.
# Mientras el número no sea correcto, se repite el proceso.
# Luego debe comprobar si el número está en una lista de números y notificarlo.

# Ejercicio 6:
# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]

# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
def ejercicio_6():
    pass

# ejercicio_6() # #-- Descomentar esta linea para ejecutar el codigo
# Llamada a funciones de cada ejercicio para pruebas
# Puedes descomentar las siguientes líneas para ejecutar los ejercicios uno por uno

# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()

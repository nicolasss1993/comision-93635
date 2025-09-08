# Ejercicio 2

# def ejercicio_2():
#     while True:
#         numero = input("Ingrese un numero impar: ") # string.
#         if numero.isdigit():
#             if int(numero) % 2 == 1:
#                 break
#             print("El numero ingresado no es impar.")
#             continue
#         print("Se introdujo un valor invalido. Por favor vuelva a intentar") 
# ejercicio_2()

"---------------------------------------------------------------------------"

# 3

# def ejercicio_3():
#     lista_impares = []
#     for i in range(1, 100, 2):
#         lista_impares.append(i)
#     print(sum(lista_impares))
# ejercicio_3()

"------------------------------------------------------------------------------"

"Otra resolucion 3"
# def ejercicio_3_a():
#     suma_total = 0
#     for numero in range(1, 101, 2):
#         suma_total += numero # suma_total = suma_total + numero
#     print(suma_total)
# ejercicio_3_a()
# print(sum(range(1,101,2)))

"-------------------------------------------------------------------------------"

# 4

def ejercicio_4():
    lista = []
    cantidad_numeros = 0
    print("Ingrese los números, presione 'Enter' luego de cada ingreso. Para realizar el cálculo escriba 'media'.")

    while True:
        numero = input("Ingrese los numeros enteros: ")
        if cantidad_numeros == 0:
            print("La media es 0 ya que no se ingreso ningun numero.")
            break
        elif len(lista) == cantidad_numeros:
            media=sum(lista)/cantidad_numeros
            print(f"La media de los números ingresados es: {media}")
            break
        elif numero.isdigit():
            lista.append(int(numero))
            continue
        else:
            print("ingrese un número válido.")
            
def ejercicio_4_a():
    contador = 0
    while True:
        cantidad_numeros=input("Ingrese un número entero: ")
        if cantidad_numeros.isdigit():
            break
        else:
            print("Debe ingresar un número")

    suma_total = 0
    
    while True:
        numero = input("Ingrese numero entero: ")
        if contador == cantidad_numeros or cantidad_numeros >= 0:
            break
        elif numero.isdigit():
            suma_total += numero
            contador += 1
    print(suma_total/cantidad_numeros)

#ejercicio_4_a()

"-----------------------------------------------------------------------------"

def ejercicio_5():
    lista_numeros = [2, 5, 6, 7]
    lista_validados = list(range(0, 10))
    while True:
        numero= input("Ingrese un número entero: ")
        if numero.isdigit():
            break
        else:
            print("Debe ingresar un número")
    while True:
        if numero in lista_validados: # numero >= 0 and numero <= 9
            break
        else:
            print("Se ingreso un numero invalido.")
    if numero in lista_numeros:
        print(f"El numero ingresado es {numero} y esta en la lista.")
    else:
        print(f"El numero {numero} NO esta en la lista.")
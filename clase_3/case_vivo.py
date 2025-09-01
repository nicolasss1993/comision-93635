"""
Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}.
Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar.
En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible.

Duración: 15 a 20 minutos
"""
diccionary_monedas = {'Dolar':'$','Euro':'€', 'Libra':'£'} # dolar, Dolar, DolaR .. 
# ... pido la info ...
# ... convierto o me aseguro de tener la info bien parseada... DolaR a Dolar. o dolar a Dolar.
# .lower = Todo a minuscula,
# .upper = TODO A MAYUSCULAS,
# .capitalize = Primer letra mayus,
# .title = Primer Letra En Mayus De Cada Caracter. 
# Pido o trato de obtener la info del diccionario
# Imprimo resultado.

# divisa = input("Ingrese divisa:")
# divisa_ok = divisa.capitalize()
# print(divisa, divisa_ok)
# valor_final = diccionary_monedas.get(divisa_ok, "La clave no existe")
# print (valor_final)



# moneda = input("Ingrese moneda: ")
# moneda= moneda[:1].upper() + moneda[1:].lower()
# print(moneda)
# # Pido o trato de obtener la info del diccionario
# print(diccionary_monedas.get(moneda))
# # Imprimo resultado.

moneda_input = input("Ingrese la divisa que desea visualizar: ").capitalize() # str(a lo que ingreso.)
moneda_seleccionada = diccionary_monedas.get(moneda_input, "La clave no existe")
print(f"La divisa es: {moneda_seleccionada}")

diccionario_monedas = {'Dolar':'$','Euro':'€', 'Libra':'£'}
while True:
    divisa_ingresada = input("Ingresar divisa").capitalize()
    valor = diccionario_monedas.get(divisa_ingresada)
    if valor != None:
        print(f"La divisa es {valor}")
        break
    print(f"La divisa {divisa_ingresada} ingresada no existe")

print("OK")
"""
A partir de una lista realizar las siguientes tareas sin modificar la lista original:

- Borrar los elementos duplicados
- Ordenar la lista de mayor a menor
- Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )
- Realizar una suma de todos los números que quedan (sum(lista))
- Añadir como primer elemento de la lista la suma realizada insert(0, suma)
- Devolver la lista modificada
- Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

Nota: Recuerda que para sumar todos los números de una lista puedes usar sum
"""
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]




"""
Consigna: Calcular el resultado de cada expresión.
En una lista encontraremos diferentes operaciones relacionales,
 calcular mentalmente el resultado de cada expresión y
 almacenarlo en una nueva lista que contendrá únicamente valores lógicos True y False.

Sugerencia. Si necesitas ayuda, deja que Python calcule estas expresiones por ti

expresiones = [
False == True,
10 >= 2*4,
33/3 == 11,
True > False,
True*5 == 2.5*2
]
"""
expresiones = [
    False == True, # False 0 == 1
    10 >= 2*4, # True
    33/3 == 11, # True
    True > False, # True
    True*5 == 2.5*2 # True
]

"""
Consigna: Crear una variable que almacene si se cumplen todas las condiciones.
A partir de dos variables llamadas NOMBRE y EDAD,
debes crear una variable que almacene si se cumplen todas las siguientes condiciones,
encadenando operadores lógicos en una sola línea:
- NOMBRE sea diferente de cuatro asteriscos ****
- Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
- EDAD sea mayor que 5 y a su vez menor que 20
- EDAD multiplicada por 3 sea mayor que 35

Desde un input conseguir las variables:

nombre = INPUT!!!
edad = INPUT!!!!
"""
# > <
NOMBRE = input("Ingrese su nombre: ")
EDAD = int(input("Ingrese su edad: "))
nombre_diferente_a_str = NOMBRE != "****"
rango_de_nombre_valido = len(NOMBRE) >= 4 and len(NOMBRE) < 8
rango_de_edad_valida = EDAD > 5 and EDAD < 20
edad_mayor_a_entero = EDAD * 3 > 35

condicion = nombre_diferente_a_str and rango_de_nombre_valido and rango_de_edad_valida and edad_mayor_a_entero
# snake_case nombrar_asi_a_las_variables
print("La condicion final es: ", condicion)
fecha_de_nacimiento = "15 de Noviembre" # Strings / Cadenas str()
nro = 1 # Enteros int()
precios = 1.75 # Flotantes / Float float()

suma = 4 + 4
resta = 4 - 4
multiplicacion = 4 * 4
division = 4 / 4
division_entera = 4.5 // 4
modulo = 5 % 3
potencia = 2 ** 2

print(potencia)
print(modulo)
print(division)

resultado = (4 + 8) / 2 * 5 ** 2 - (9 + 3) / 2
resultado_1 = (4 + 8 / 2) * 5 ** 2 - (9 + 3) / 2
print(resultado, resultado_1)

# var = int(input("Ingrese un numero: ")) # str()
# print(var + 5, type(var))
# Esta variable sirve para guardar un nombre.
#nombre = input("Cual es tu nobmre: ")

#print(nombre + "Tu cumpleaños es: " + fecha_de_nacimiento) # 3 var
#print(f'{nombre} tu cumpleaños es: {fecha_de_nacimiento}') # f-string

nombre = "Nicolas"
        # 0123456
print(nombre)
#print(nombre[0:4:2]) # Slicing [comienzo : hasta : salto]
#print(nombre[::-1]) # Da vuelta la cadena
nombre = nombre[:4] # "Nico"
print(nombre)
# print(len(nombre))

cadena = 'Hola, Mundo Como Estas ?' # int() str() float()
# print(cadena.upper())
# print(cadena.lower())
# print(nombre.replace('Nico', 'Mico'))
# print(nombre.find('c'))
# print("40".isdigit())

lista_str = cadena.split(" ")
print(len(lista_str))
print(lista_str)
print(" ".join(lista_str))


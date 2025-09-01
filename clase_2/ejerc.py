"""
Actividad: Desafío de Listas
Consigna:
En esta actividad, podrás poner en práctica lo aprendido. Usaremos Visual Studio Code.
Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras.
Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.
- Añade a la lista_1 el 456789 y luego el "Hola Mundo"
- Luego añade a la lista_2 el "Hola y adiós", y luego el 5555
- Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
- Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
- Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3

"""
lista_1 = [5, 6, 7, 9]
lista_2 = ["Nicolas", "Ezequiel"]
lista_1.extend([456789, "Hola mundo"])
# lista_1.append(456789)
# lista_1.append("Hola mundo")
print(lista_1)
lista_2.extend(["Hola y adiós", 5555])
print(lista_2)

lista_3 = lista_1[:len(lista_1)-1]
print(lista_3)

lista_4 = lista_2[1:len(lista_2)-1]
print(lista_4)

lista_5 = lista_4 + lista_3
print(lista_5)
"""
Actividad: Desafío de Tuplas
Consigna:
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

- El último ítem de tupla
- El número de ítems de tupla
- La posición donde se encuentra el ítem 87 de tupla
- Una lista con los últimos tres ítems de tupla
- Un ítem que haya en la posición 8 de tupla
- El número de veces que el ítem 7 aparece en tupla
- Copia esta tupla para iniciar el ejercicio:

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

"""
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)
print(tupla[-1])
print(len(tupla))
print(tupla.index(87))
conversion_a_lista= list(tupla)
print(conversion_a_lista[len(tupla)-3:])
print(tupla[8])
print(tupla.count(7))
"""
Actividad: Dicts
Consigna:

Trabajaremos con el notebook de la sesión, específicamente sobre la temática de Diccionarios.
Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018. Y mostrarlo por pantalla.

Datos para la resolución:

1990: 'Alemania',
1994: 'Brasil',
1998: 'Francia',
2002: 'Brasil',
2006: 'Italia',
2010: 'España',
2014: 'Alemania'
2018: 'Francia'
2022: 'Argentina'
"""
diccionario = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia',
    "2022": 'Argentina'
}

print(diccionario)
"""
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

Partirás de:

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

Debes llegar a:

matriz = [
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]

"""

lista = [
    [1, 5, 1], # 0
    [2, 1, 2], # 1
    [3, 0, 1], # 2
    [1, 4, 4] # 3
]

lista[0].append(sum(lista[0]))
lista[1].append(sum(lista[1]))
lista[2].append(sum(lista[2]))
lista[3].append(sum(lista[3]))
print(lista)


var = "hola que tal".split(" ")
var[0] = var[0].capitalize()
print(var)
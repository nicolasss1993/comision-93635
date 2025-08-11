"""
Actividad extra: Desafío Slicing
Consigna: Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.

cadena = "acitametaM ,5.8 ,otipeP ordeP"

Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1]

Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno

Extraer la nota y almacenarla en una variable llamada nota.

Extraer la materia y almacenarla en una variable llamada materia.

Mostrar por pantalla la siguiente estructura, usando la concantenación de cadenas:

NOMBRE APELLIDO ha sacado un NOTA en MATERIA
"""

cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]
print(cadena_volteada)
"Pedro Pepito, 8.5, Matematica"
#[0:5] - Nombre, Apellido [6:12]
cadena_split = cadena_volteada.split(",")
nombre_apellido = cadena_split[0]
nota = cadena_split[1].replace(" ", "")
materia = cadena_split[2].strip()  # "   Nicolas  ".strip() = "Nicolas"
print(f"{nombre_apellido.upper()} ha sacado un {nota} en {materia}") # print(" una cadena")
print(nombre_apellido.upper(),"ha sacado un", nota, "en",materia) # print(var, cadena, var, cadena, var)

# print(cadena_split)
# nombre = f'{cadena_volteada[0:5]} {cadena_volteada[6:12]}'
# nombre_1 = cadena_volteada[0:5]
# apellido = cadena_volteada[6:12]
# nombre_alumno = nombre_1 + " " + apellido
# print(nombre_alumno)
# print(nombre)
# nota = float(cadena_volteada[14:17])
# print(nota)

https://drive.google.com/drive/folders/1X42ldyFil8i6soLU2h1pDpFtccsZ5UI8?usp=sharing
"""
Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:
Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación:

nota_1 cuenta como el 20% de la nota final

nota_2 cuenta como el 30% de la nota final

nota_3 cuenta como el 50% de la nota final

Aspectos a incluir
Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto.
Los datos deben guardarse en variables y deben ser dinámicos por medio de input.
"""
# int = 4, 5, 10, 650 flaot = 2.2, 10.5, 6.66, etc...
nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))
nota_final = (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)

print ("La nota final es : " , nota_final)
print(f'La nota final es: {nota_final}')
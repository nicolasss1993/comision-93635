# control_de_flujo.py

# Unidad 4: Control de Flujo en Python

# Actividad 1: Generaciones digitales
# Consigna: Determinar a qué generación pertenece una persona según su año de nacimiento.
# Nota: Si el año no corresponde a ninguna generación conocida, se indica "No existe generación asociada".


ano_nacimiento = 1990
ano_nacimiento = 2015
ano_nacimiento= 1940
















# """
# Determina la generación según el año de nacimiento.
# """
if 1946 <=  ano_nacimiento <= 1964:
    print("Baby Boomer")
elif 1965 <= ano_nacimiento <= 1980:
    print("Generación X")
elif 1981 <= ano_nacimiento <= 1996:
    print("Generación Y")
elif 1997 <= ano_nacimiento <= 2012:    
    print("Generación Z")
elif 2013 <= ano_nacimiento <= 2025:
    print("Generación Alpha")
else:
    print("No existe generación asociada")
    

# Actividad 2: Crédito Bancario
# Consigna: Aprobar o denegar un crédito bancario en función de la edad, antigüedad en el sistema financiero y los ingresos.

edad = 18
antiguedad = 21
ingreso = 3000
# """
#     Determina si se aprueba un crédito según criterios de edad, antigüedad y nivel de ingresos.
# """
if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500:
        print("Crédito aprobado")
    elif antiguedad < 3 and ingreso > 4000:
        print("Crédito aprobado")
    else: 
        print("Crédito denegado")
else:
    print("Crédito denegado")
 

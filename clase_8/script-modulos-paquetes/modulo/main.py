# import ope

# resultado = ope.sumar(4, 5)
# print(f"La suma es: {resultado}")


from ope import sumar, restar
from cosas.mate import multiplicar # * significa dame todo del archivo. (funciones, variables globales, etc.)

resultado = sumar(4, 5)
print(f"La suma es: {resultado}")

resultado = restar(4, 5)
print(f"La suma es: {resultado}")

resultado = multiplicar(2, 5)
print(f"La multiplicacion es {resultado}")

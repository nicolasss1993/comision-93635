from calculadora import Calcuradora, restar, sumar
# from calculadora.resta import Calcuradora, restar
# from calculadora.suma import sumar
from funciones_validar import validar_numero

resultado = sumar(4, 5)
print(f"La suma es: {resultado}")

resultado = restar(4, 5)
print(f"La resta es: {resultado}")

calc = Calcuradora(5, 5)
print(calc)
print(calc.sumar())

print(validar_numero(3))
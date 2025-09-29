# =========================================
# MÉTODOS Y ATRIBUTOS EN PYTHON
# =========================================

# 1) ATRIBUTOS:
# - Son variables asociadas a una clase o a una instancia (objeto).
# - Pueden ser:
#   * De instancia -> propios de cada objeto.
#   * De clase -> compartidos por todos los objetos de la clase.

class Persona:
    # Atributo de clase (compartido por todas las instancias)
    especie = "Humano"
    cant_personas = 0

    def __init__(self, nombre, edad, dni): # magic methods / metodos magicos
        # Atributos de instancia (propios de cada objeto)
        self.id = Persona.cant_personas
        Persona.cant_personas += 1
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def __str__(self): # print(Persona("Nicolas", 30))
        return f"Soy {self.nombre} y tengo {self.edad} años. ID: {self.id}"


# Uso
# p1 = Persona("Ana", 25, "134123")
# p2 = Persona("Luis", 30, "111111")
# print(p1)
# print(p2)
# print(p1.nombre)        # Ana  (atributo de instancia)
# print(p2.nombre)        # Luis
# print(p1.especie)       # Humano (atributo de clase)
# print(p2.especie)       # Humano
# print(Persona.especie)


# 2) MÉTODOS:
# - Funciones definidas dentro de una clase.
# - Tipos:
#   * De instancia -> acceden y modifican atributos del objeto (self).
#   * De clase -> trabajan a nivel de clase, usan cls en lugar de self.
#   * Estáticos -> no acceden ni a la clase ni a la instancia directamente.


class Calculadora:
    # Atributo de clase
    historial = []

    def __init__(self, valor):
        self.valor = valor  # atributo de instancia

    # Método de instancia
    def sumar(self, numero):
        self.valor += numero
        Calculadora.historial.append(f"Suma: {numero}")
        return self.valor

    # Método de clase
    @classmethod
    def ver_historial(cls): # Calculadora
        return cls.historial # Calculadora.historial

    # Método estático
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0


# Uso
calc = Calculadora(10)
print(calc.sumar(5))             # 15
print(calc.sumar(20))            # 35

# Método de clase (se llama con la clase directamente o con el objeto)
print(Calculadora.ver_historial())  # ['Suma: 5', 'Suma: 20']
print(calc.mostrar_historial())

# Método estático
print(Calculadora.es_par(10))    # True
print(calc.es_par(7))            # False


# =========================================
# RESUMEN
# =========================================
# - Atributos de instancia: únicos de cada objeto.
# - Atributos de clase: compartidos por todos los objetos.
# - Métodos de instancia: usan self, acceden a datos de un objeto.
# - Métodos de clase: usan cls, acceden a la clase en general.
# - Métodos estáticos: no usan ni self ni cls, son funciones auxiliares.

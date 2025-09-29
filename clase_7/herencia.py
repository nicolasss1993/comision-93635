"""
Herencia en Programación Orientada a Objetos (POO)
-------------------------------------------------

La herencia es un mecanismo que permite a una clase (llamada CLASE HIJA o DERIVADA) 
heredar atributos y métodos de otra clase (llamada CLASE PADRE o BASE). 

Esto permite **reutilizar código** y crear jerarquías de clases más organizadas.

Características:
- La clase hija hereda todos los atributos y métodos de la clase padre.
- La clase hija puede añadir nuevos atributos y métodos.
- La clase hija puede redefinir (sobrescribir) métodos del padre → esto se llama OVERRIDE.
- Facilita la reutilización de código y la extensibilidad.

Ejemplo de herencia simple:
"""

# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"- {self.nombre}"

    def hacer_sonido(self):
        return "Sonido genérico"

# Clase hija (hereda de Animal)
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def __str__(self):
        return f"Gato: {self.nombre}"

    def hacer_sonido(self):
        return "Miau!"

# Uso
p = Perro("Firulais")
g = Gato("Michi")
a = Animal("Un animal")
print(a.nombre, ":", a.hacer_sonido())
print(p.nombre, ":", p.hacer_sonido())   # Firulais : Guau!
print(g.nombre, ":", g.hacer_sonido())   # Michi : Miau!
print(p)
print(g)
print(a)


"""
Beneficios de la herencia:
- Reutilización de código (no repetir lo mismo en varias clases).
- Facilita la organización en jerarquías.
- Posibilidad de polimorfismo: distintas clases pueden comportarse de manera diferente 
  con los mismos métodos (ej: todos los animales tienen "hacer_sonido()", 
  pero cada uno lo implementa distinto).
-------------------------------------------------
Herencia múltiple
-------------------------------------------------
En Python una clase puede heredar de más de una clase padre.

Se usa cuando necesitamos combinar comportamientos de varias clases.

Python resuelve conflictos de métodos mediante el **MRO (Method Resolution Order)**, 
que define el orden en el que se buscan métodos y atributos.

Ejemplo:
"""

# Clase padre 1
class Mamifero:
    def amamantar(self):
        return "Alimentando crías con leche"

    def saludar(self):
        print("Hola...")

# Clase padre 2
class Ave:
    def volar(self):
        return "Volando por los cielos"

    # def saludar(self):
    #     print("Hola que tal...")

# Clase hija que hereda de dos clases
class Murcielago(Mamifero, Ave): # no es lo mismo que hacer Murcielago(Ave, Mamifero): 
    def hacer_sonido(self):
        return "Chillido ultrasónico"

    # def saludar(self):
    #     print("Un muercielago saludando")

m = Murcielago()
print(m.amamantar())   # de Mamifero
print(m.volar())       # de Ave
print(m.hacer_sonido()) # propio de Murcielago
m.saludar()


"""
Beneficios de la herencia múltiple:
- Permite combinar comportamientos de distintas clases.
- Evita tener que reescribir código en varias clases diferentes.
- Muy útil en casos donde un objeto comparte características de varios tipos 
  (ejemplo: Murciélago es Mamífero y Ave a la vez).

Precauciones:
- Puede generar ambigüedad si varias clases padres tienen el mismo método → 
  Python usa el **MRO** para decidir el orden.
- Se recomienda no abusar de la herencia múltiple, y preferir composición 
  en casos más complejos.
"""

# Composicion

class Vehiculo:
    def __init__(self, color, motor):
        self.color = color
        self.motor = motor
        #self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color} Con un motor {self.motor.potencia} HP!"
    def arrancar(self):
        print(f"Auto {self.color} arracando...")
        self.motor.encender()


class Motor: # motor = Motor("155")
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        print(f"Motor de {self.potencia} HP encendido")

class Ruedas:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    
    def rodar(self):
        print(f"La rueda de {self.tamaño} pulgadas esta rodando.")

motor = Motor("150")
auto = Vehiculo("blanco", motor)
print(auto)
auto.arrancar()
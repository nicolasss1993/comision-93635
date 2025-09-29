# Asociacion
"""
Un Profesor enseña a un Alumno.
El profesor puede existir sin el alumno y viceversa.

"""

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def ensenar(self, alumno):
        print(f"{self.nombre} enseña a {alumno.nombre}")

    def saludar(self):
        print(f"Hola me llamo {self.nombre}")

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

prof = Profesor("Ana")
alumno = Alumno("Juan")
prof.ensenar(alumno)

# Agregacion

"""
Una Escuela tiene Profesores.
Si la escuela cierra, los profesores pueden trabajar en otro lugar.
"""

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

prof1 = Profesor("Ana")
prof2 = Profesor("Luis")

escuela = Escuela("Colegio Central")
escuela.agregar_profesor(prof1)
escuela.agregar_profesor(prof2)

# Composicion

"""
Un Coche tiene un Motor.
Si el coche deja de existir, el motor también.
"""

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("150HP") 

auto = Coche("Toyota")
print(auto.motor.potencia)

# Generalizacion / Herencia

"""
Perro y Gato son Animales.
Comparten características pero cada uno puede tener comportamientos propios.
"""

class Animal: # Clase Padre
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        print(f"{self.nombre} se mueve")

class Perro(Animal): # Clase Hijo de Animal
    def ladrar(self):
        print("Guau!")

class Gato(Animal): # Clase Hija de Animal
    def maullar(self):
        print("Miau!")

perro = Perro("Firulais")
perro.mover()
perro.ladrar()

gato = Gato("Mishi")
gato.mover()
gato.maullar()

for animal in [Perro("Firulais"), Perro("Fede"), Gato("Mishi"), Gato("algo")]:
    animal.mover()

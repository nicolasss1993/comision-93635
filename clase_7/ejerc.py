"""
Actividad: Implementación en Python

Implementar la Clase de Alumno, directamente en Python.

Aclaraciones Generales:
- El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
- El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos de 5 puntos desaprueba la materia, más de 5 puntos aprueba.
    Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
- Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.

"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"El estudiante: {self.nombre} tiene una nota de {self.nota}.")
    
    def resultado(self):
        if self.nota >= 5:
            return "Estas aprobado"
        return "Estas desaprobado"

alumno_1 = Alumno("Nicolas D", 6)
alumno_2 = Alumno("Nicolas Z", 4)
alumno_3 = Alumno("Federico", 5)

lista_a = [alumno_1, alumno_2, alumno_3]

for alumno in lista_a:
    alumno.imprimir()
    print(alumno.resultado())
    print("*"*15)
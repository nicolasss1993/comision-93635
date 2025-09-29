class Auto: # auto_1 = Auto()
    # Atributo de clase.
    CANTIDAD_RUEDAS = 4

    def __init__(self, color, año):
        # Atributos de instancia.
        self.color = color
        self.año = año
    
    def ver_info(self): # Metodo de instancia.
        print(f"El auto es de color: {self.color} y año: {self.año}")

    @classmethod
    def obtener_cantidad_ruedas(cls): # Metodo de clase. cls - class
        return cls.CANTIDAD_RUEDAS

    @staticmethod
    def encender():
        print("Encendio")

class Moto:
    def __init__(self, color, año):
        self.color = color
        self.año = año

    def ver_info(self, nombre):
        print(f"La moto es de color: {self.color} y año: {self.año}")
        print(f"Y es de {nombre}")

moto = Moto("Azul", "2020")
auto = Auto("Blanco", 2022)
auto_2 = Auto("Gris", 2021)
print(moto.color)
print(auto.año)
moto.ver_info("Nicolas")
auto.ver_info()
print(auto.CANTIDAD_RUEDAS, auto_2.CANTIDAD_RUEDAS)
Auto.CANTIDAD_RUEDAS = 5

print(auto.CANTIDAD_RUEDAS, auto_2.CANTIDAD_RUEDAS)

print(Auto.obtener_cantidad_ruedas())

class Calculadora:
    def __init__(self, valor):
        self.valor = valor
    
    @staticmethod
    def es_par(numero):
        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")

# calc = Calculadora(10)
# Calculadora.es_par(5)
# calc.es_par(4)
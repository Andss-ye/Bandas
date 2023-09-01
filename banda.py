from musico import Musico
from instrumento import Instrumento
from random import choice, randint

class Banda:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.integrantes = []
        self.instrumentos = instrumentos
    def tocar(self):
        pass
    def crear(self):
        for i in range(0, randint(1, 10)):
            self.integrantes.append(Musico("Juan",choice(self.instrumentos)))
            

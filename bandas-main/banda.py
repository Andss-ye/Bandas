from musico import Musico
from instrumento import Instrumento
from random import choice, randint

class Banda:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.integrantes = ["Julian", "Roberto", "Cristian", "Manuel", "Andrés"]
        self.musicos = []
        self.instrumentos = instrumentos
    def tocar(self):
        pass
    def crear(self):
        for i in range(0, randint(1, 5)):
            instrumento_random = choice(self.instrumentos)
            for i in range(0, randint(1,5)):
                nombre_random = choice(self.integrantes)
            musico = Musico(nombre_random, instrumento_random)
            self.musicos.append(musico)

    def afinar_instrumentos(self):
        for musico in self.musicos:
            musico.afinar_instrumento()

    def consultar(self):
        print("Nombre de la banda: ", self.nombre)
        print("Instrumentos en la banda: ", [instrumento.nombre for instrumento in self.instrumentos])
        print("Integrantes de la banda: ", [(musico.nombre, musico.instrumento_toca.nombre) for musico in self.musicos])

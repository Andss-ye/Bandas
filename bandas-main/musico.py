class Musico:
    def __init__(self, nombre, instrumento_toca):
        self.nombre = nombre
        self.instrumento_toca = instrumento_toca

    def tocar(self):
        print(f"{self.nombre} está tocando {self.instrumento_toca.nombre}")

    def afinar_instrumento(self):
        self.instrumento_toca.afinar()

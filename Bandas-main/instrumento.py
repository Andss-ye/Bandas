class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
    def afinar(self):
        pass
    def tocar(self):
        pass
    def consultar(self):
        print("Soy: ", self.nombre)

class Piano(Instrumento):
    def __init__(self):
        super().__init__("Piano")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")

class Saxofon(Instrumento):
    def __init__(self):
        super().__init__("Saxofon")

class Bajo(Instrumento):
    def __init__(self):
        super().__init__("Bajo")

if __name__ == "__main__":
    a = Piano()
    a.consultar()
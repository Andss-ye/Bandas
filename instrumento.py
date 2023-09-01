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
    def __init__(self, nombre):
        super().__init__(nombre)

class Guitarra(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

class Saxofon(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

class Bajo(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

if __name__ == "__main__":
    a = Piano("Piano")
    a.consultar()
    
class Instrumento:
    def __init__(self, nombre, puede_afinar = False):
        self.nombre = nombre
        self.puede_afinar = puede_afinar

    def afinar(self):
        if self.puede_afinar == True:
            print(f"Afinando {self.nombre}")
        else:
            print(f"{self.nombre} no se puede afinar")
    def tocar(self):
        pass
    def consultar(self):
        print("Soy: ", self.nombre)

class Piano(Instrumento):
    def __init__(self, puede_afinar):
        super().__init__("Piano", False)

class Guitarra(Instrumento):
    def __init__(self, puede_afinar):
        super().__init__("Guitarra", True)

class Saxofon(Instrumento):
    def __init__(self, puede_afinar):
        super().__init__("Saxofon", False)

class Bajo(Instrumento):
    def __init__(self, puede_afinar):
        super().__init__("Bajo", False)

if __name__ == "__main__":
    a = Piano()
    a.consultar()
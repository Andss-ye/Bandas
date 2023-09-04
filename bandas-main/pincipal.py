from banda import *
from instrumento import *

if __name__ == "__main__":
    # Crear una banda con algunos instrumentos
    b = Banda("Los Rítmicos", [Piano(False), Guitarra(False), Saxofon(False), Bajo(False)])
    
    # Crear músicos aleatorios
    b.crear()
    
    # Consultar la información inicial de la banda
    b.consultar()
    
    # Dar la opción de afinar los instrumentos
    opcion = input("¿Deseas afinar los instrumentos de la banda? (S/N): ").strip().lower()
    
    if opcion == 's':
        b.afinar_instrumentos()  # Llama al método para afinar los instrumentos
    else: 
        b.afinar_instrumentos()

    
    # Consultar la información actualizada de la banda
    b.consultar()

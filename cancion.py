from contenido import Contenido

class Cancion(Contenido):
    def __init__(self, titulo, duracion, genero):
        super().__init__(titulo, duracion)
        self.genero = genero
 
    def reproducir(self):
        print(f"Reproduciendo canción: {self.titulo}")
 
    def mostrar_informacion(self):
        print("\n---Cancion---")
        print(f"Canción: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Duración: {self.duracion}")
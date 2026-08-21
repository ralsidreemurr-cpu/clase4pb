from contenido import Contenido

class Podcast(Contenido):
    def __init__(self, titulo, duracion, categoria, numero_episodio):
        super().__init__(titulo, duracion)
        self.categoria = categoria
        self.numero_episodio = numero_episodio
 
    def reproducir(self):
        print(f"Reproduciendo podcast: {self.titulo}"
              f"  Episodio {self.numero_episodio}")
 
    def mostrar_informacion(self):
        print("\n---Podcast---")
        print(f"titulo: {self.titulo}")
        print(f"Categoria: {self.categoria}")
        print(f"Duración: {self.duracion}")
        print(f"Episodio: {self.numero_episodio}")
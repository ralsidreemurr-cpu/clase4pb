class Contenido:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
 
    def reproducir(self):
        print(f"Reproduciendo: {self.titulo}")
 
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")  
        print(f"Duración: {self.duracion}")
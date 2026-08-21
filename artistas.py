class Artista:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        self.canciones = []
 
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"'{cancion.titulo}'fue asosiada"
              f"al artista {self.nombre}")
 
    def mostrar_informacion(self):
        print("\n---Artista---")
        print(f"Artista: {self.nombre}"
              f" Género: {self.genero}"
              f"Canciones: {len(self.canciones)}")

        if len(self.canciones) == 0:
            print("Notiene canciones registradas")
        else:
            for cancion in self.canciones:
                print(f"-{cancion.titulo}")
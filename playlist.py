class Playlist:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"'{cancion.titulo}' fue agregada a la playlist '{self.nombre}'")

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            print(f"'{cancion.titulo}' fue eliminada de la playlist '{self.nombre}'")
        else:
            print(f"'{cancion.titulo}' no está en la playlist '{self.nombre}'")

    def mostrar_playlist(self):
        print("\n---Playlist---")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Canciones: {len(self.canciones)}")

        if len(self.canciones) == 0:
            print("No tiene canciones registradas")
        else:
            for cancion in self.canciones:
                print(f"-{cancion.titulo}"
                      f"{cancion.genero}")
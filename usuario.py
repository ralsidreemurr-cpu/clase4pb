from playlist import Playlist


class Usuario:
    def __init__(self, nombre, correo, premium=False):
        self.nombre = nombre
        self.correo = correo
        self.premium = premium
        self.playlists = []

    def crear_playlist(self, nombre, descripcion):
        nueva_playlist = Playlist(nombre, descripcion)
        self.playlists.append(nueva_playlist)
        print(f"Playlist '{nombre}' fue creada por {self.nombre}")
        return nueva_playlist

    def mostrar_informacion(self):
        print("\n---Usuario---")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Premium: {'Sí' if self.premium else 'No'}")
        print(f"Playlists: {len(self.playlists)}")

        if len(self.playlists) == 0:
            print("No tiene playlists creadas")
        else:
            for playlist in self.playlists:
                print(f"-{playlist.nombre}")
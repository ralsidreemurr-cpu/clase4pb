from artistas import Artista
from cancion import Cancion
from podcast import Podcast
from contenido import Contenido
from playlist import Playlist
from album import Album
from usuario import Usuario


def main():
    cancion1 = Cancion("El Fin En Pie", "3:39", "Remix")
    cancion2 = Cancion("Rey de Cenizas", "4:15", "Remix")
    cancion3 = Cancion("Hueso cansado", "3:39", "Remix")
    cancion4 = Cancion("Martillo de la justicia", "7:32", "Remix")

    artista = Artista("CaixoTrilogy", "Remix")

    artista.agregar_cancion(cancion1)
    artista.agregar_cancion(cancion2)
    artista.agregar_cancion(cancion3)
    artista.agregar_cancion(cancion4)

    podcast1 = Podcast("Funa2", "1:35:55", "Comedia", 4)

    print()
    cancion1.reproducir()
    cancion1.mostrar_informacion()

    print()
    cancion2.reproducir()
    cancion2.mostrar_informacion()

    print()
    cancion3.reproducir()
    cancion3.mostrar_informacion()

    print()
    cancion4.reproducir()
    cancion4.mostrar_informacion()

    print()
    podcast1.reproducir()
    podcast1.mostrar_informacion()

    print()
    artista.mostrar_informacion()

    album1 = Album("Caixo", 2024)
    album1.agregar_cancion(cancion1)
    album1.agregar_cancion(cancion2)
    album1.mostrar_album()

    print()

    usuario1 = Usuario("Camila Rojas", "camila@correo.com", premium=True)
    playlist1 = usuario1.crear_playlist("Favoritas de Remix", "Mis canciones remix favoritas")

    playlist1.agregar_cancion(cancion1)
    playlist1.agregar_cancion(cancion3)
    playlist1.agregar_cancion(cancion4)
    playlist1.eliminar_cancion(cancion4)

    print()
    playlist1.mostrar_playlist()
    usuario1.mostrar_informacion()


if __name__ == "__main__":
    main()
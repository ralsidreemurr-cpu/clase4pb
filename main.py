from artistas import Artista
from cancion import Cancion
from podcast import Podcast
from contenido import Contenido


def main():
    cancion1 = Cancion("El Fin En Pie", "3:39", "Remix")
    cancion2 = Cancion("Rey de Cenizas", "4:15", "Remix")
    cancion3 = Cancion("Hueso cansado", "3:39", "Remix")
    cancion4 = Cancion("Martillo de la justicia", "7:32", "Remix")

    artista = Artista("CaixoTrilogy", "Remix")
    
    artista.agregar_cancion(cancion1)
    artista.agregar_cancion(cancion2)

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


if __name__ == "__main__":
    main()
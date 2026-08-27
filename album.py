class Album:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio
        self.canciones = []

    def agregar_cancion(self, cancion):
          self.canciones.append(cancion)
          print(f"'{cancion.titulo}' fue agregada al álbum '{self.titulo}'")
  
      def mostrar_album(self):
          print("\n---Álbum---")
          print(f"Título: {self.titulo}")
          print(f"Año: {self.anio}")
          print(f"Canciones: {len(self.canciones)}")
  
          if len(self.canciones) == 0:
              print("No tiene canciones registradas")
          else:
              for cancion in self.canciones:
                  print(f"-{cancion.titulo}")
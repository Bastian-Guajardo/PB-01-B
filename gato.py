from mascota import mascota

class gato:

   def __init__(self, pelaje, cant_vidas):
        self.pelaje = pelaje
        
        self.__cant_vidas = cant_vidas
        
   def descripcion(self):
        print(f"{self.pelaje} - {self.__cant_vidas} vidas")

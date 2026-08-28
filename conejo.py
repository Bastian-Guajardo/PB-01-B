
from mascota import mascota
class conejo:
    
    def __init__(self, pelaje, tipo_alimentacion):
        self.pelaje = pelaje

        self.__tipo_alimentacion = tipo_alimentacion
        
    def descripcion(self):
        print(f"{self.nombre} - {self.raza} - {self.edad} años")
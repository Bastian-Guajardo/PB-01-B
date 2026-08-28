from mascota import mascota

class perro:
    pass
    def __init__(self, tamaño, cantidad_vacunas):
        self.tamaño = tamaño
        self.__cantidad_vacunas = cantidad_vacunas

    def get_cantidad_vacunas(self):
        print(self.__cantidad_vacunas)
        
    def set_cantidad_vacunas(self, cantidad):
            pass
    
    def descripcion(self):
        print(f" tamaño: {self.tamaño} - vacunas: {self.__cantidad_vacunas}")
        # validamos si nuestra lista tiene objetos en el inventario
    if len(self.__cantidad_vacunas) == 0:
            print("La mascota no posee vacunas")
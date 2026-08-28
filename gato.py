from mascota import Mascota
from reglas import Regla_Valor


class gato(Mascota):
    def __init__(self, nombre, edad, raza, peso, costo_consulta, pelaje, vidas):
        super().__init__(nombre, edad, raza, peso, costo_consulta)
        
        if not Regla_Valor(vidas):
            print("[Error] El numero de vidas debe ser un numero mayor a cero.")
            return
        
        self.pelaje = pelaje
        self.vidas = vidas
        
        
    def descripcion(self):
        # Muestra una descripcion de la mascota
        
        return f"Nombre: {self.nombre} - Color: {self.color_pelaje} - Vidas: {self.vidas}"
    
    
    def mostrar_informacion(self):
        # Muestra toda la informacion de la mascota
        
        print("\n=== Informacion Paciente ===\n")
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}\n"
              f"Raza: {self.raza}\n"
              f"Peso: {self.peso}\n"
              f"Color: {self.color_pelaje}\n"
              f"Vidas: {self.vidas}")

from mascota import Mascota, mascota


class conejo(Mascota):
    def __init__(self, nombre, edad, raza, peso, costo_consulta, color_pelaje, tipo_alimentacion):
        super().__init__(nombre, edad, raza, peso, costo_consulta)
        
        # Verifica que el campo tipo_alimentacion no este vacio
        if not tipo_alimentacion.split():
            print("[Error] El valor no puede estar vacio")
            return

        self.color_pelaje = color_pelaje
        self.tipo_alimentacion = tipo_alimentacion
        
        
    def descripcion(self):
        # Muestra una descripcion de la mascota
        
        return f"Nombre: {self.nombre} - Color: {self.color_pelaje} - Alimentacion: {self.tipo_alimentacion}"
    
    
    def mostrar_informacion(self):
        # Muestra toda la informacion de la mascota
        
        print("\n=== Informacion Paciente ===\n")
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}\n"
              f"Raza: {self.raza}\n"
              f"Peso: {self.peso}\n"
              f"Color: {self.color_pelaje}\n"
              f"Alimentacion: {self.tipo_alimentacion}")
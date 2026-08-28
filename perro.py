from mascota import Mascota
from reglas import Regla_Valor


class perro(Mascota):  
    def __init__(self, nombre, edad, raza, peso, costo_consulta, tamaño, cantidad_vacunas):
        super().__init__(nombre, edad, raza, peso, costo_consulta)
        
        if not Regla_Valor(cantidad_vacunas):
            print("[Error] El numero de vacunas debe ser un numero mayor a cero.")
            return
        
        self.tamaño = tamaño
        self.cantidad_vacunas = cantidad_vacunas
        
        
    def descripcion(self):
        # Muestra la descripcion
        
        return f"Nombre: {self.nombre} - Tamaño: {self.tamaño} - Vacunas: {self.cantidad_vacunas}"
    
    
    def mostrar_informacion(self):
        # Muestra la informacion
        
        print("\n=== Informacion Paciente ===\n")
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}\n"
              f"Raza: {self.raza}\n"
              f"Peso: {self.peso}\n"
              f"Tamaño: {self.tamaño}\n"
              f"Numero vacunas: {self.cantidad_vacunas}")
    
    
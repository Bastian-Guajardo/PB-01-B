from mascota import Mascota


class AplicacionMascotas:
    def __init__(self):
        self.mascotas = []
        
        
    def agregar_mascota(self, mascota:Mascota):
        # Agrega un objeto de clase Mascota a la lista de mascotas
        
        self.mascotas.append(mascota)
        print(f"Se agregó {mascota.nombre} al sistema")
    
    
    def mostrar_catalogo(self):
        # Muestra todos los registros
        
        if len(self.mascotas) == 0:
            print("No hay mascotas registradas en el sistema")
        else:
            print("\n=== Mascotas Registradas ===")
            print(f"Numero de registros: {len(self.mascotas)}\n")
            for mascota in self.mascotas:
                print(f"* {mascota.descripcion()}")
                print(f"* Valor consulta: ${mascota.get_costo_consulta()}\n")
            print("-- Fin registros --\n")
    
    
    def calcular_costo_total(self):
        # Suma y devuelve el valor de consulta de todas las mascotas registradas
        
        if len(self.mascotas) == 0:
            return "No hay mascotas registradas en el sistema"
        else:
            costo_total = 0
            for mascota in self.mascotas:
                costo_total += mascota.get_costo_consulta()
                
        return costo_total
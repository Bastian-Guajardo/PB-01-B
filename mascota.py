from reglas import Regla_Valor


class Mascota:

    def __init__(self, nombre, edad, raza, peso, costo_consulta):
        
        if not Regla_Valor(costo_consulta):
            print("ERROR tu valor debe ser un numero mayor a cero")
            return
        
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.__costo_consulta = costo_consulta


    def get_costo_consulta(self):
        # Devuelve el valor 
        
        return self.__costo_consulta


    def set_costo_consulta(self, costo):
        # Valida que el valor cumpla la regla
        
        if not Regla_Valor(costo):
            print("ERROR tu valor debe ser un numero mayor a cero")
            return
        
        self.__costo_consulta = costo
        print(f"Costo consulta actualizado {costo}")


    def descripcion(self):
        # Muestra la descripcion
        
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad} años"
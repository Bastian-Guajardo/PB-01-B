class Mascota:

    def __init__(self, nombre, edad, raza, peso, costo_consulta):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.__costo_consulta = costo_consulta

    def get_costo_consulta(self):
        print(self.__costo_consulta)

    def set_costo_consulta(self, costo):
            pass

    def descripcion(self):
        print(f"{self.nombre} - {self.raza} - {self.edad} años")
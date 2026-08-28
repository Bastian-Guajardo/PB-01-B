
class AplicacionMascotas:

    def __init__(self):
        self.mascota= []

    def agregar_mascotas(self, mascota ):

        self.mascota.append(mascota)

        print(f"{mascota.nombre} ha sido agregada al registro")

    def mostrar_mascotas(self):

        print("\n ---MASCOTAS---")
        # validamos si nuestra lista tiene Mascotas en el registro
        if len(self.mascota) == 0:
            print("no hay mascotas")

        else:
            # recorremos el arreglo de objetos
            for mascota in self.mascota:
                print(f"- {mascota.nombre} ({mascota.tipo})")
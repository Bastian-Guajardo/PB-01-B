# Alumno Bastian Guajardo
# git: https://github.com/Bastian-Guajardo/PB-01-B.git
from perro import perro
from gato import gato
from conejo import conejo
from mascota import Mascota
from aplicacion_mascotas import AplicacionMascotas

def main():
    try:
    
    # APLICACION
        app = AplicacionMascotas()
    
        
        perro_1 = perro("edgar",6,"shar pie",25,420)
        
        perro_2 = perro("Rafael",8,"bulldog",32,550)
        
        conejo_1 = conejo ("carlos",10,"de nieve",15,200)
        
        gato_1 = gato(" bastian",4,"egipcio",10,100) 
        
        print("\n DESCRIPCION DE LAS MASCOTAS \n")
        
        print(perro_1.descripcion())
        print(perro_2.descripcion())
        print(gato_1.descripcion())
        print(conejo_1.descripcion())
    
    
        print("\n # modificacion consulta #")
        
        print(" error invalido\n")
        
        perro_2.set_costo_consulta(0)

        print("\n Valor de la consulta \n")
        
        perro_2.set_costo_consulta(100)
        
        
        print("\n Agregar una mascota \n")
        
        app.agregar_mascota(perro_1)
        
        app.agregar_mascota(perro_2)
        
        app.agregar_mascota(gato_1)
        
        app.agregar_mascota(conejo_1)
    

        print("\n Mostrar el catalogo y la consulta ")
        
        app.mostrar_catalogo()
        
        costo_total = app.calcular_costo_total()
        print(f"Costo total de consultas: ${costo_total}")
        
    except ValueError as e:
        print(e)
    
    
if __name__ == "__main__":
    main()
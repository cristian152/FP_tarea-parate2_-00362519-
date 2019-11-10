
import os
def menu():

    os.system('clear') 
    print("BIENVENIDO A CINELAND")
    print("el prcio es 4.87")
    print("\t1 - para ver las peliculas disponibles")
    print("\t0 - salir")
    
def pelicula():
    print("Las peliculas de hoy son:" )
    
def opcionPelicula():
    print("Gran eleccion")
    
while True:
    menu()
    opcionMenu = input("Seleccione una de nuestra clasificaciones >> ")
    
    if opcionMenu=="1":
        print("")
        print("\nLas peliculas disponibles para el dia de hoy son:")
        print("1-John Wick 2\n2- El Joker 3\n3-Avenger (end game)")
        opcionPelicula= int(input("Seleccione una pelicula a ver: "))
        if opcionPelicula==1:
            print("Esperemos disfrute de 1-John Wick")
            print("Disfrute de su pelicula")
                
        if opcionPelicula==2:
            print("Esperemos disfrute de El Joker")
            print("Disfrute de su pelicula")
                
        if opcionPelicula==3:
            print("Esperemos disfrute de Avenger (end game)")
            print("Disfrute de su pelicula")
            
            
        mayores()
    elif opcionMenu=="0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
print("vuelva pronto")


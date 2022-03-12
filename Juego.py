

#Procedimiento para el menu
def menu():
  Bandera=False
  while (Bandera!=True):
    print("")
    print("\033[;36m"+"Bienvenido al juego de piedra, papel o tijera")
    print("")
    print("1. Iniciar juego")
    print("2. Salir del juego")
    print("")
    opcion=int(input("Seleccione una opcion:"))
    if opcion==1:
      cleaning()
      jugar="si"
      preguntar_nombre()
      while jugar=="si":
        iniciar_juego()
        print("")
        jugar=input("jugar otra ? (si/no): ")
        cleaning()

    if opcion==2:
      Bandera=True

import os, sys

def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


#Aqui empieza todo
menu()
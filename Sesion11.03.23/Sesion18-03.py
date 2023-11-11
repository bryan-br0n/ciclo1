print("Bienvenido al restaurante")

print('''
      \tMenu
      1- Especialidad
      2- Bebidas
      ''' )
menu = str(input("Ingrese una Opcion del menu -> ")).lower()
if menu == "especialidad" or menu == "1":
    print('''Menu de Especialidad
            1- Mar y Tierra
            2- Pupusas
            ''')
    menu2 = input("\nIngrese una opcion del menu -> ").lower()

    if menu2 == "1" or menu2 == "mar y tierra":
       print("Usted eligio el plato de Mar y Tierra")

    elif menu2 == "2" or menu2 == "pupusas":
        print("Usted eligio Pupusas")
    else:
        print("La opción no se encuentra disponible")

elif menu == 'bebidas' or menu == '2':
    print('''Menu de Bebidas
            1- Coca Cola
            2- Pepsi
            ''')  
    menu2 = input("Ingrese una opcion del menu -> ").lower()

    if menu2 == "1" or menu2 == "cocacola":
        print("Usted eligio la bebida Coca Cola")

    elif menu2 == "2" or menu2 == "pepsi":
        print("Usted eligio la bebida Pepsi")
    else:
        print("La opción no se encuentra disponible")

else:
    print("La opcion no se encuentra disponible")

print("Fin del Programa :)")

users = [{"id":"1","nombre":"Nicolas","password":"Nico123","tipo_usuario":"Administrador","estado":"A"},
        {"id":"2","nombre":"Rolando","password":"Rolando123","tipo_usuario":"Gerente","estado":"A"},
        {"id":"3","nombre":"Gerardo","password":"Gerardo123","tipo_usuario":"Cajero","estado":"I"},
        {"id":"4","nombre":"Josue","password":"Josue123","tipo_usuario":"Cajero","estado":"A"}]
areas = [
    {"id":"1","area":"Componentes"},
    {"id":"2","area":"Perifericos"},
    {"id":"3","area":"Enfriamientos"},
]

categorias = [
    {"id":"1","categoria":"Procesadores","id_areas":"1"},
    {"id":"2","categoria":"Motherboards","id_areas":"1"},
    {"id":"3","categoria":"Mouses","id_areas":"2"},
    {"id":"4","categoria":"Teclados","id_areas":"2"},
    {"id":"5","categoria":"Enfriamiento por aire","id_areas":"3"},
    {"id":"6","categoria":"Enfriamiento Liquido","id_areas":"3"},
]

productos = [
    {"id":"1","id_categorias":"1","nombre":"Ryzen 3 3200G","proveedor":"AMD","fecha_caducidad":"N/A","fecha_entrada":"1-5-2023","detalle":"Procesador con arquitectura Zen 3 y graficos integrados Vega 8","precio":90.50,"unidades":4},
    {"id":"2","id_categorias":"1","nombre":"Intel Core i3 12100F","proveedor":"Intel","fecha_caducidad":"N/A","fecha_entrada":"1-5-2023","detalle":"Procesador sin graficos integrados con socket LGA1700","precio":159,"unidades":3}
]


def login():
    while True:
        nombreUser = input("Ingresa el nombre de usuario: ")
        password = input("Ingresar Contraseña de usuario: ")
        for usuario in users:
            if usuario["nombre"] == nombreUser and usuario["password"] == password:
                print(f"Inicio de sesión exitoso.\n Bienvenido {usuario['nombre']}")
                View1(usuario["tipo_usuario"])
                return
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

#Funcion donde se Crean,Leen,Actualizan y Eliminan Usuarios
def CrudUser(accion):
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                try: 
                        #Crear un nuevo usuario
                        nombre = input("Ingresa el nombre del usuario: ")
                        contra = input("Ingresar contraseña de usuario: ")
                        print("nivel de usuario\n1- Administrador\n2- Gerente\n3- Cajero")
                        continuar = True
                        while continuar == True:
                            k = input("Ingrese el numero de nivel de usuario: ")
                            if k == "1":
                                tipo_usuario = "Administrador"
                                continuar == False
                                break
                            elif k == "2":
                                tipo_usuario = "Gerente"
                                continuar == False
                                break
                            elif k == "3":
                                tipo_usuario = "Cajero"
                                continuar == False
                                break
                            else:
                                print("la opcion ingresada no existe,Vuelve a intentarlo")

                        
                        users.append({"id":len(users) + 1,"nombre":nombre,"password":contra,"tipo_usuario":tipo_usuario,"estado":"A"},)
                        x = users[-1]
                        
                        #Mostrando datos del usuario ingresado#
                        print("Nombre:",x["nombre"],"\nContraseña:",x["password"],"\nNivel de usuario:",x["tipo_usuario"],"\nEstado:",x["estado"])
                        print("!Usuario Ingresado con exito!")
                        ViewAdmin()
                            
                        
                except:
                    print("ocurrio un error")
                
            case "2":
                #Actualizar un nuevo usuario
                print("-------------------------------------------")
                print("\tLista de Usuarios")
                print("-------------------------------------------")
                print("Id\tnombre\t Contraseñas\t Tipo usuario")
                for j in range(len(users)):
                    print ("{:<7} {:<8} {:<15} {:<15}".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario']))
                usuarioUpd = input("Ingresa el 'id' del usuario para actualizarlo: ")
                x =users[int(usuarioUpd)-1]
                print(f"Nombre actual: {x['nombre']}")
                x['nombre']= input(f"Ingresar nuevo nombre: ")
                print(f"Contraseña actual: {x['password']}")
                x['password']= input(f"Ingresar nueva contraseña: ")
                print(f"Tipo de Usuario actual: {x['tipo_usuario']}")
                x['tipo_usuario']= input(f"Ingresar nuevo tipo de usuario: ")
                print(f"Estado actual: {x['estado']}")
                x['estado']= input(f"Ingresar estado de usuario: ")
                users[int(usuarioUpd)-1] = x
                print(users[int(usuarioUpd)-1])
                ViewAdmin()  
            case "3":
                #Eliminar un usuario
                print("-------------------------------------------")
                print("\tLista de Usuarios")
                print("-------------------------------------------")
                print("Id\tnombre\t Contraseñas\t Tipo usuario")
                for j in range(len(users)):
                    print ("{:<7} {:<8} {:<15} {:<15}".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario']))
                usuarioUpd = input("Ingresa el 'id' del usuario para Eliminarlo: ")
                users.pop(int(usuarioUpd)-1)
                ViewAdmin()
                
            case "4":
                print ("{:<8} {:<10} {:<15} {:<15}".format( "Id","Nombre","Contraseña","Tipo Usuario"))
                for j in range(len(users)):
                    print ("{:<8} {:<10} {:<15} {:<15}".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario']))
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case _:
                print("La opcion ingresada no existe, Vuelve a intentarlo: ")
#Funcion donde se Crean,Leen,Actualizan y Eliminan areas
def CrudArea(accion):
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                #crear una area
                #{"id":"1","area":"Componentes"},
                area = input("Ingrese el nombre de la nueva area: ")
                areas.append({"id":len(areas) + 1,"area":area},)
                x = areas[-1]
                print("print",x)
                 #Mostrando datos del usuario ingresado#
                print("Id:",x['id'],"Nombre del area:",x['area'])
                print("!Area Registrada con exito!")
                ViewAdmin()
                
            case "2":
                 #Actualizar una area
                print("-------------------------------------------")
                print("\tLista de areas")
                print("-------------------------------------------")
                print ("{:<4} {:<15}".format( "Id","area"))
                print("Id\tnombre\t Contraseñas\t Tipo usuario")
                for j in range(len(areas)):
                    print ("{:<4} {:<15} ".format( areas[j]['id'],areas[j]['area']))
                areaUpd = input("Ingresa el 'id' del area para actualizarlo: ")
                id =areas[int(areaUpd)-1]
                print(f"Nombre actual del area: {id['area']}")
                id['area']= input(f"Ingresar nombre del area: ")
                areas[int(areaUpd)-1] = id
                #print(areas[int(areaUpd)-1])
                print("Area actualizada con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()  
                
            case "3":
                #Opcion 3 Desactivar area#
                ##Falta terminarlos##
                print ("{:<4} {:<20}".format( "Id","area"))
                for j in range(len(areas)):
                    print ("{:<4} {:<20}".format( areas[j]['id'],areas[j]['area']))
                areaUpd = input("Ingresa el 'id' del area para desactivar: ")
                
                    
                id = areas[int(areaUpd)-1]
                print(f"Nombre actual del area: {id['area']}")
                id['area']= input(f"Ingresar nombre del area: ")
                
                
            case "4":
                #  Opcion 4 Mostras las areas#
                print ("{:<4} {:<20}".format( "Id","area"))
                for j in range(len(areas)):
                    print ("{:<4} {:<20}".format( areas[j]['id'],areas[j]['area']))
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case _:
                print()

def CrudCategorias(acccion):
    seguir = True
    while seguir == True:
        match acccion:
            case "1":
                #Crear categoria nueva
                categoria = input("Ingrese el nombre de la nueva categoria: ")
                 #relacion de area con categorias por medio del id_area
                j = 1
                for area in areas:
                    print(f"{j}-{area['area']}")
                    j += 1
                id_area = input("Ingrese el area a la que pertenece: ")
                categorias.append({"id":len(categorias) + 1,"categoria":categoria,"id_area":id_area},)
                data = categorias[-1]
                 #Mostrando datos del usuario ingresado# <+++++++ areglar estilo con .format()*************
                for j in areas:
                    if data["id_area"] == j["id"]:
                         print("Id:",data['id'],"Categoria:",data['categoria'],"area",j['area'])
                print("!Categoria Registrada con exito!")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "2":
                #Actualizar categoria 
                #  {"id":"1","categoria":"Procesadores","id_areas":"1"},
                print("-------------------------------------------")
                print("\tLista de Categorias")
                print("-------------------------------------------")
                print ("{:<4} {:<25} {:<15}".format( "Id","categorias","areas"))
                for j in range(len(categorias)):
                    for i in areas:
                        if categorias[j]["id_areas"] == i["id"]:
                            print ("{:<4} {:<25} {:<15} ".format( categorias[j]['id'],categorias[j]['categoria'],i['area']))
                catUpd = input("Ingresa el 'id' de la categoria para actualizarlo: ")
                id = categorias[int(catUpd)-1]
                print(f"Nombre actual de la categoria: {id['categoria']}")
                id['categoria']= input(f"Ingresar nombre de la categoria: ")
                #relacion de area con categorias por medio del id_area
                j = 1
                for area in areas:
                    print(f"{j}-{area['area']}")
                    j += 1
                id_area = input("Ingrese el area a la que pertenece: ")
                id['id_areas']= id_area
                categorias[int(catUpd)-1] = id
                print("Area actualizada con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()       
            case "3":
                #Desactivar categoria 
                #  {"id":"1","categoria":"Procesadores","id_areas":"1"},
                print()
            case "4":
                #Mostrar categorias
                
                print ("{:<8} {:<25} {:<15} ".format( "Id","Categoria","Area"))
                for j in range(len(categorias)):
                    for area in areas:
                        if categorias[j]['id_areas'] == area['id']:
                            print("{:<8} {:<25} {:<15}".format( categorias[j]['id'],categorias[j]['categoria'],area['area']))
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()

def CrudProductos(accion):
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                #Crear producto nuevo
                 #relacion de categoria con producto 
                j = 1
                for cat in categorias:
                    print(f"{j}-{cat['categoria']}")
                    j += 1
                id_cat = input("Ingrese el numero de la categoria : ")
                nombreProduct = input("Ingrese el nombre del producto: ")
                proveedor = input("Ingrese el nombre del proveedor: ")
                fecha_caducidad = "N/A"
                fecha_entrada = input("Ingrese la fecha de entrada *1-1-2020*: ")
                detalle = input("Ingrese el detalle del producto: ")
                #Validar que sea numeros decimales#
                follow = True
                while  follow == True:
                    try:
                        precio = float(input("Ingrese el precio del producto: "))
                        follow = False
                        break
                    except:
                        print("El dato ingresado con tiene letra,Vuelve a intentarlo")
                follow_unid = True
                while follow_unid == True:
                    try:
                        unidades = int(input("Ingrese las unidades de productos"))
                        follow_unid = False
                        break
                    except:
                        print("El dato ingresado con tiene letra,Vuelve a intentarlo")
                productos.append({"id":len(productos) + 1,"categoria":id_cat,"nombre":nombreProduct,"proveedor":proveedor,"fecha_caducida":fecha_caducidad,"fecha_entrada":fecha_entrada,"detalle":detalle,"precio":precio,"unidades":unidades},)
                data = productos[-1]
                 #Mostrando datos del usuario ingresado# <+++++++ areglar estilo con .format()*************
                for j in categorias:
                    if data["id_categoria"] == j["id"]:
                         print ("{:<4} {:<25} {:<15} ".format( data['id'],j['categoria'],data['nombre'],data['proveedor'],data['fecha_caducida'],data['fecha_entrada'],data['detalle'],data['precio'],data['unidades']))
                         #print("Id:",data['id'],"Categoria:",data['categoria'],"area",j['area'])
                print("!Categoria Registrada con exito!")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "2":
                #Actualizar categoria 
                #  {"id":"1","categoria":"Procesadores","id_areas":"1"},
                print("-------------------------------------------")
                print("\tLista de Categorias")
                print("-------------------------------------------")
                print ("{:<4} {:<25} {:<15}".format( "Id","categorias","areas"))
                for j in range(len(categorias)):
                    for i in areas:
                        if categorias[j]["id_areas"] == i["id"]:
                            print ("{:<4} {:<25} {:<15} ".format( categorias[j]['id'],categorias[j]['categoria'],i['area']))
                catUpd = input("Ingresa el 'id' de la categoria para actualizarlo: ")
                id = categorias[int(catUpd)-1]
                print(f"Nombre actual de la categoria: {id['categoria']}")
                id['categoria']= input(f"Ingresar nombre de la categoria: ")
                #relacion de area con categorias por medio del id_area
                j = 1
                for area in areas:
                    print(f"{j}-{area['area']}")
                    j += 1
                id_area = input("Ingrese el area a la que pertenece: ")
                id['id_areas']= id_area
                categorias[int(catUpd)-1] = id
                print("Area actualizada con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()       
            case "3":
                #Desactivar categoria 
                #  {"id":"1","categoria":"Procesadores","id_areas":"1"},
                print()
            case "4":
                #Mostrar productos
                
                print ("{:<8} {:<25} {:<25} {:<15} {:<15} {:<15} {:<15} {:<15} ".format( "Id","Categoria","Nombre","Proveedor","F.Caducida","F.Entrada","Precio","Unidades"))
                for j in range(len(productos)):
                    for cat in categorias:
                        if productos[j]['id_categorias'] == cat['id']:
                            print("{:<8} {:<25} {:<25} {:<15} {:<15} {:<15} {:<15} {:<15}".format( productos[j]['id'],cat["categoria"],productos[j]['nombre'],productos[j]['proveedor'],productos[j]['fecha_caducidad'],productos[j]['fecha_entrada'],productos[j]['precio'],productos[j]['unidades']))
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
                
#menu de vista admin
def ViewAdmin():
    seguir = True
    print("¿Que accion quieres realizar?: ")
    print("""
    1- Consultar Usuarios
    2- Consultar Areas
    3- Consultar Categorias
    4- Consultar Productos
    """)
    while seguir == True:
        consulta = input("Ingresa una accion: ")
        match consulta:
            case "1":
                print("""
            ¿Que desea hacer?
        1- Crear un Usuario        
        2- Actualizar un Usuario
        3- Eliminar un Usuario
        4- Mostrar Usuarios
                """)
                accion = input("Ingresar accion a realizar: ")
                CrudUser(accion)
                
            case "2":
                print("""
            ¿Que desea hacer?
        1- Crear una area        
        2- Actualizar area
        3- Eliminar area (todavia no sirve)
        4- Mostrar areas
                """)
                accion = input("Ingresar opcion a realizar: ")
                CrudArea(accion)
            case "3":
                print("""
            ¿Que desea hacer?
        1- Crear una categoria        
        2- Actualizar una categoria
        3- Eliminar una categoria
        4- Mostrar categorias
                """)
                accion = input("Ingresar opcion a realizar: ")
                CrudCategorias(accion)
            case "4":
                print("""
            ¿Que desea hacer?
        1- Crear un producto        
        2- Actualizar un producto
        3- Eliminar un producto
        4- Mostrar productos
                """)
                accion = input("Ingresar opcion a realizar: ")
                CrudProductos(accion)
                
            case _:
                print("La opcion ingresada no existe, Vuelve a intentarlo")
                
def ViewManager():
    print("¿Que accion quieres realizar?: ")
    print("""
    1- Consultar Areas
    2- Consultar Categorias
    3- Consultar Productos
    4- Cerrar session
    """)
    
    follow = True
    while follow:
        consulta = input("Ingresa una la accion que quieras realizar: ")
        match consulta:
            case "1":
                i = 1
                print("----------------------------------")
                print("\tConsulta de areas")
                print("----------------------------------")
                for area in areas:
                    print ("{:<7} {:<8}".format( i, area['area']))       
                    i += 1
                print("--------------------------------------------------------")
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "2":
                i = 1
                print("=======================================================")
                print("\tConsulta de Categorias")
                print("=======================================================")
                print ("{:<3} {:<25} {:<15}".format( "Id","Categorias","Areas"))
                print("--------------------------------------------------------")
                for cat in categorias:
                    for j in areas:
                        if j['id'] == cat['id_areas']:
                            print ("{:<3} {:<25} {:<15}".format( i, cat['categoria'],j['area']))       
                    i += 1
                print("--------------------------------------------------------")
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "3":
                i = 1
                print("==================================")
                print("\tConsulta de productos")
                print("==================================")
                print ("{:<3} {:<25} {:<15} {:<12} {:<12} {:<8} {:<8} ".format( "Id","producto","proveedor","F.caducidad","F.entrada","Precio","Unidades"))
                print("--------------------------------------------------------------------------")
                for prod in Productos:
                    
                    print ("{:<3} {:<25} {:<15} {:<12} {:<12} {:<8} {:<8}  ".format( i, prod['nombre'],prod['proveedor'],prod['fecha_caducidad'],prod['fecha_entrada'],prod['precio'],prod['unidades'],))       
                    i += 1
                print("--------------------------------------------------------------------------")
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "4":
                print("Cerrando Session...")
                login()
            case _:
                print("La opcion Ingresada no existe vuelva a intentarlo")
def ViewCashier():
    print()


#Funcion de vista 1
def View1(tipo_user):
    match tipo_user:
        case "Administrador":
            ViewAdmin()
        case "Gerente":
            ViewManager()
        case "Cajero":
            print("Ingresaste como cajero")
        case _:
            print("La opcion ingresada no existe, Vuelve a intentarlo")
login()
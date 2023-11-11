print("******************************")
print("*Sistema control de vacaciones*")
print("******************************")

nomEmpleado = str(input("Por favor introduce tu nombre: "))
print("Claves de departamento\n 1. Atencion al cliente\n 2. ventas\n 3. Gerencia")
clavEmpleado = int(input("Por favor introduce la clave de departamento "))
añosEmpleado = int(input("Por favor introduce tus años de servicio "))


if clavEmpleado == 1:
    #aqui ira el desarrollo
    if añosEmpleado == 1 and añosEmpleado <2:
        print("El empleado ", nomEmpleado, " tiene derecho a 6 dias de vacaciones")
    elif añosEmpleado >= 2 and añosEmpleado <=6:
        print("El empleado ", nomEmpleado, " tiene derecho a 14 dias de vacaciones")
    elif añosEmpleado >=7:
        print("El empleado ", nomEmpleado, " tiene derecho a 20 dias de vacaciones")
    else:
        print("aun no cumples un año de servicio")
elif clavEmpleado == 2:
    #desarrollo
    if añosEmpleado == 1 and añosEmpleado <2:
        print("El empleado ", nomEmpleado, " tiene derecho a 6 dias de vacaciones")
    elif añosEmpleado >=2 and añosEmpleado <=6:
        print("El empleado ", nomEmpleado, " tiene derecho a 14 dias de vacaciones")
    elif añosEmpleado >=7:
        print("El empleado ", nomEmpleado, " tiene derecho a 20 dias de vacaciones")
    else:
        print("aun no cumples un año de servicio")
elif clavEmpleado == 3:
    #desarrollo
    if añosEmpleado == 1 and añosEmpleado <2:
        print("El empleado ", nomEmpleado, " tiene derecho a 6 dias de vacaciones")
    elif añosEmpleado >=2 and añosEmpleado <=6:
        print("El empleado ", nomEmpleado, " tiene derecho a 14 dias de vacaciones")
    elif añosEmpleado >=7:
        print("El empleado ", nomEmpleado, " tiene derecho a 20 dias de vacaciones")
    else:
        print("aun no cumples un año de servicio")
else:
    print("La clave del departamento no existe, vuelva a intentarlo")

#Programa de numeros naturales
cantidad_num = int(input("Ingresa la cantidad de números: "))
i = 1
nums = []
#Pidiendo al usuario que ingrese los digitos a evaluar
while i <= cantidad_num:
    while True:
        numero = input(f"Ingrese su {i}° numero: ")
        if numero.isalpha() == True :
           print("!! El valor ingresado no es un numeros, Ingrese un numero !!")
        else:
            if int(numero) < 0:
                nums.append(int(numero))
                break
            nums.append(int(numero))
            break
        # if tipo == "int":
        #     nums.append(numero)
        # else:
        #     print("!! El valor ingresado no es un numero !!")
    i += 1
#evaluando si lo numeros son positivos negativos o nulos
positivos = sum(1 for x in nums if x > 0)
negativos = sum(1 for x in nums if x < 0)
nulos = sum(1 for x in nums if x == 0)
    
# Mostrar los resultados
print("================================================================")
print("====================       Resultados      =====================")
print("================================================================")


print(f"La Cantidad de numeros positivos que Ingresastes son: {positivos}")
print(f"La Cantidad de numeros negativos que Ingresastes son: {negativos}")
print(f"La Cantidad de numeros nulos que Ingresastes son: {nulos}")

    
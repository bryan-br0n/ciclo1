'''#calcular hipotenusa
cat1 = float(input("Ingrese el valor del primer cateto -> "))
cat2 = float(input("Ingrese el valor del segundo cateto -> "))

while cat1 <= 0 or cat2 <= 0:
    print("Los valores ingresados no son validos, ambos catetos deben ser mayores")
    cat1 = float(input("Ingrese el valor del primer cateto -> "))
    cat2 = float(input("Ingrese el valor del segundo cateto -> "))

hipo = (cat1**2 + cat2**2)**0.5
print(f"La hipotenusa del triangulo rectangulo es: {hipo}")


#calculadora
import math
while True:
    print("Bienvenido a su calculadora")
    a = float(input("ingrese el valor de A -> "))
    b = float(input("ingrese el valor de B -> "))

    while True:
        menu = input(
                Menu
                1- Calcula la raiz cuadrada de la suma A y B
                2- Calcula A / B
                3- Calcular la siguiente formula: ( A * B ) / 2.5
                4- Salir
                Que operacion desea realizar -> )
        
        if menu == "1":
            res = math.sqrt(a + b)
            print(f"El resultado es {res}")
            break

        elif menu == "2":
            if b != 0:
                res = a / b 
                print(f"El resultado es: {res}")
                break
            else:
                print("El divisor no puede ser 0")
        
        elif menu == "3":
            res = (a + b)/ 2.5
            print(f"El resultado es: {res}")
            break

        elif menu == "salir" or menu == "4":
            print("Gracias por utilizar la calculadora")
            exit()

        else:
            print("Opcion invalida, ingrese una de las que se encuentra en el menu")'''


#bucle for
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
for i in lista:
    for j in i:
    print(i)

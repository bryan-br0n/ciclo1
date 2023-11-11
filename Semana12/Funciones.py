#Funciones en python
def Mensaje():
    print("Hola Grupo Fundamentos de programacion")

Mensaje()

def Nombre(nombre):
    print("Hola", nombre)

Nombre("Ana Yancy")

entradaNombre = input("Ingresa tu nombre -> ")
Nombre(entradaNombre)


def Multiplicar(numero, multi):
    print(f"{numero}*{multi} = {numero*multi}")

print("Comienza el programa")
Multiplicar(6, 4)
print("Otra forma")
Multiplicar(int(input("Dame un numero -> ")), int(input("Dame otro numero -> ")))
print("Fin")


def suma(a,b):
    resultado = a + b
    return resultado

print("la suma es -> ", suma(5, 5))

resuSuma = suma(6,9)
print("La suma es -> ", resuSuma)

def es_polidromo(cadena):
    cadena = cadena.lower().replace(" ","")
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_polidromo(texto):
    print("El texto es un polindromo")
else:
    print("El texto no es un polindromo")


def validaCorreo():
    #Ejemplo validacion de correo
    email = False

    for i in "mauricio@gmail.com":
        if i == "@":
            email = True

    if email == True:
        print("El email es correcto")
    else:
        print("El email es incorrecto")

validaCorreo()
print("fin")

def validaCorreo2():
    valido = False
    email = input("Digite su correo -> ")
    for i in range(len(email)):
        if email[i] == "@":
                valido = True
        if valido == True:
            print("Email es correcto")
        else:
            print("email incorrecto")

validaCorreo2()
print("fin")
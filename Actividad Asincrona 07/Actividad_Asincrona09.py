#Damos la bienvenida al programa
print("-----------------------")
print("Bienvenido al programa ")
print("-----------------------")

#Definimos variables para solicitar informacion
nombre1 = input("Ingrese su nombre -> ")
apellido1 = input("Ingrese su apellido -> ")
edad1 = int(input("¿Cual es su edad? "))
sexo1 = input("¿Cual es su sexo? ")

#damos informacion solicitada
print("Su nombre es:", nombre1, apellido1, " su edad es:", edad1, " y su sexo es:", sexo1, )

#rango de etapa del usuario
if edad1 <= 2:
    print(nombre1, "Usted se encuentra en la etapa de Bebe")
elif edad1 >=3 and edad1 <=5:
    print(nombre1, "Usted se encuentra en la etapa de: Infancia")
elif edad1 >=6 and edad1 <=11:
    print(nombre1, " Usted se encuentra en la etapa de: Niñes")
elif edad1 >=12 and edad1 <=18:
    print(nombre1, " Usted se encuentra en la etapa de: Adolescencia")
elif edad1 >=19 and edad1 <=26:
    print(nombre1, " Usted se encuentra en la etapa de: Juventud")
elif edad1 >=27 and edad1 <=40:
    print(nombre1, " Usted se encuentra en la etapa de: Adultez Joven")
elif edad1 >=41 and edad1 <=55:
    print(nombre1, " Usted se encuentra en la etapa de: Adultez")
elif edad1 >=56 and edad1 <=65:
    print(nombre1, " Usted se encuentra en la etapa de: Persona Mayor")
elif edad1 >=66:
    print(nombre1, " Usted se encuentra en la etapa de: Tercera edad")
else:
    print("Exediste los años")


#definimos si la edad es par o impar
if edad1 %2==0:
        print("Su edad", edad1, "es par")
else:
        print("Su edad", edad1, "es impar")



print("Fin del programa :)")
cadena1 = "Tengo una gatita que se llama luna" #Declaracion de variable
print(cadena1)

#lista1 = [] #Lista vacia

lista1 = ['Pera', 'Manzana', 'Naranja', 'Uva']
print(lista1)

Longitud = len(cadena1) #Devolver la longitud de una lista
print(Longitud)

elementos = len(lista1) #Devuelve el numero de elementos de la lista
print(elementos)

cuenta = cadena1.count("luna") #Cuenta cuantas veces aparece la palabra luna
print(cuenta)
print(cadena1.find('luna')) #Devuelve la posicion de busqueda

cadena2 = cadena1.join("**") #Coloca la variable entre los caracteres definidos
print(cadena2)

lista2 = cadena1.split(" ") #Divide la cadena por cada espacio y crea un elemento de la lista
print(lista2)

Cadena3 = cadena1.replace("a","o",1) #Busca y sustituye el valor cuantas veces sera sustituido
print(Cadena3)

cadena4 = "Mar" #variable mAr maR mar MAR Mar
print(cadena4.upper()) #Covierte a Mayuscula
print(cadena4.lower()) #Convierte a Minuscula

lista3 = ['Fundamnetos', 2, True, 2.2] #Lista heterogenea 
print(lista3)
print(lista3[0])

lista4 = [1,2,3,4,5] #Lista homegenea (en este caso numerica)
print(lista4)
print(lista4[-1])

lista5 = ["nombre", "Apellido", ["Tel", "Direc"]] #Declarando una lista dentro de otra lista
print(lista5)
print(lista5[2][0])

print(lista4[1:3:1]) #Responde al patron inicio:fin:pasos
print(lista5[1][1:5:2]) #La posicion de la variable inicio:fin:pasos

lista3[2] = False #Cambia el valor de un elemento de la lista
print(lista3)

lista4[-2] = lista4[-2] + 1
print(lista4)

lista4[-3] = lista4[-3] - 1
print(lista4)

lista4.pop(0)
print(lista4)

lista3.remove(0) #
print(lista3)

lista3 = lista3 + [6]
print(lista3)

lista3.append(7)
print(lista3)

lista3.extend([8,9])
print(lista3)

lista3.insert(1, "Programacion")
print(lista3)

lista3[:] = []
print(lista3)
print(lista1.count(2))
print(lista1.index("Pera"))

lista4.sort() #se ordena la lista
print(lista4)
lista4.reverse()
print(lista4)

tupla1 = (1,2,3)
print(tupla1)

tupla2 = 1,2,3
print(tupla2)

tupla3 = []
tupla4 = tuple()
tuple5 = tuple([1,2,3,4,5]) 
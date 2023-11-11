#Estructura de control IF o Sentencia simple
print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cual es tu nombre? ")

funProgra = int(input(nombre + " ¿Cual es tu calificación en Fundamentos de Programacion? "))
mate = int(input(nombre + " ¿Cual es tu calificación en Matemática? "))
ingles = int(input(nombre + " ¿Cual es tu calificación en Ingles? "))

promedio = (funProgra + mate + ingles)/3
#print(promedio)

if promedio >= 6:
    print("Felicidades "+ nombre + " Aprobastes con un Promedio de: ", promedio)
 
print("fin")

variableString = "'Esto resalta' el texto"
variableString1 = '"Esto resalta" el texto'
print(variableString)
print(variableString1)
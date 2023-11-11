#Este es un ejemplo de condicional compuesta
print("sistema para calcular el promedio de alumnos")
nombre = input("Danos tu nombre -> ")

mate = float(input(nombre + " ¿Cual es tu nota en Matematica? "))
fisi = float(input(nombre + " ¿Cual es tu nota en Fisica? "))
quimi = float(input(nombre + " ¿Cual es tu nota en Quimica? "))

promedio = (mate + fisi + quimi)/3

if promedio >=6:
    print("Felicidades " + nombre + " Aprobaste con un promedio de: ", promedio)
    print("Felicidades " + nombre + " Aprobaste con un promedio de: ", round(promedio, 2))
else:
    print("Lo sentimos", nombre, " no aprobaste, tu promedio fue de: ", promedio)
    print("Lo sentimos", nombre, "no aprobaste, tu promedio fue de: ", round(promedio, 2))

print("Fin")
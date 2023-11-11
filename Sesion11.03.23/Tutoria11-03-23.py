not1 = float(input("Ingrese su nota 1 -> "))
not2 = float(input("\nIngrese su nota 2 -> "))
not3 = float(input("\nIngrese su nota 3 -> "))
not4 = float(input("\nIngrese su nota 4 -> "))

#round

promedio = (not1 + not2 + not3 + not4)/4

if promedio >= 6:
    print(f"\nUsted aprobo la materia con un promedio de {round(promedio, 2)}")

else:
    print("\nUsted no aprobo el curso, su promedio fue de ", promedio)

print("\nFin del programa")

#.lower() sirve para convertir toda cadena de caracteres o letras en minusculas

fruta = input("Ingrese su fruta ->").lower()

if fruta == 'sandia':
    print("Eligio sandia")
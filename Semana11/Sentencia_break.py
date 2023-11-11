'''#ejemplo para break 
print("while con la sentencia break")
contador = 0

while contador < 10:
    contador +=1
    if contador == 5:
        break
    print("Valor actual de la variable-> ", contador)

print("Fin del programa")'''

#Ejemplo para continue
print("while con la sentencia continue")
cont = 0

while cont < 10:
    cont +=1
    if cont == 5:
        continue
    print("valor actual de la variable -> ", cont)

print("fin del programa, la sentencia continue se ha ejecutado")
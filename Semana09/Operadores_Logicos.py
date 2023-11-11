print("Introduce dos numeros a comparar")

numUno = int(input("Introduce el primer numero -> "))
numDos = int(input("Introduce el segundo numero -> "))

print("\n Los numeros a comparar son -> ", numUno, " y ", numDos, "\n")
#print("\n Los numeros a comparar son -> "+ str(numUno) + " y " + str(numDos) + "\n")

if numUno == numDos:
    print("Los numeros son iguales...")
if numUno != numDos:
    print("Los numeros son diferentes...")
if numUno > numDos:
    print("Es mayor")
if numUno < numDos:
    print("Es Menor")
if numUno >= numDos:
    print("Es Mayor o igual...")
if numUno <= numDos:
    print("Es Menor o igual...")
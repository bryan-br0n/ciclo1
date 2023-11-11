#from numpy import*
import numpy as np
x = np.array([3,4,9,7,2,6,1,5])
print(x)

#creacion de un arreglo fila
v = np.array([3,6,7,2,8])
print(v)

#usando Zeros(n)
print(np.zeros(6))

#usando unos(n)
print(np.ones(5))

#usando arange(a,b,c)
print(np.arange(3.0,9.0))

#usando linspace
print(np.linspace(1,2,5))

a = np.array([55,21,19,11,6])
b = np.array([12,-9,0,22,-9])

#suma los dos arreglos elemento a elemento
print(a + b)
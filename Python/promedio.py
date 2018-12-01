#!/usr/bin/python
n = int(input('ingrese la cantidad de datos: '))
suma = 0
for i in range(n):
    x = float(input('ingrese datos: '))
    suma = suma + x
    print (suma)
prom = suma / n
print ('prommedio es: ', prom)

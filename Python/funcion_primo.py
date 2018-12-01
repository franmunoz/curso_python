#!/usr/bin/python
a = 0
b = 0
x = int(input('ingrese un nro para la siguiente la funcion f(x)=2*X^2-1: '))
def f(x):
    y = 2 * x ** 2 -1
    return y
print ('evaluando funcion y=f(x)')
y = f(x)
print (y,x)
print ('se evaluara el nro', y)
for i in range (y):
    i = i+1
#    print ('evaluando en numero',i)
    primo = y%i
    if primo == 0:
        a = a+1
if a > 2:
    print ('cantidad de residuos en 0', a)
    print ('no es primo')
else:
    print ('es primo')
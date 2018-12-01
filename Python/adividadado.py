#!/usr/bin/python
from random import *
intento = 0
x = 0
dado1 = randint(1,6)
print ('lanzando el dado......')
#print ('el dado salio', dado)
while x != dado1:
    x = int(input('ingresa unl nro: '))
    print ('fallaste')
    intento = intento +1
else:
    print ('acertaste en el intento', intento)
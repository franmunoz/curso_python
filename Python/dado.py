#!/usr/bin/python
from random import *
#apuesta = int(input('ingrese un monto: '))
n = int(input('ingrese cantidad de intentos '))
gana = 0
for i in range (n):
    x = randint (1, 6)
    print ('intento nro', i+1)
    print ('en el dado ha salido un', x)
    if x == 6:
        gana = gana + 600
        print ('has ganado 600')
    elif x == 3:
        gana = gana + 300
        print ('has ganado 300')
    elif x == 1:
        print ('siga participando')
    else:
        gana = gana - 50
        print ('pierdes 50')
    print ('por ahora tiene', gana)
    print (' ')
if gana > 0:
    print ('la ganancia total es ', gana)
else:l
    print ('ha perdido', gana)

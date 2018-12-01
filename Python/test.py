from random import *
x = 0
i = 0
while True:
    x = randint (1, 6)
    print (x)
    i = i+1
    if x == 3:
        print ('salio 3! en el intento', i)
        break

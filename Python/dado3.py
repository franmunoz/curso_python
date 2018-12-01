from random import *
intento = int(input('ingrese intentos: '))
for i in range(intento):
    dado = randint (1, 6)
    print ('en el dado salio', dado)
    if dado == 3:
        print ('salio 3 !!!, esto se acabo ')
        break 
if dado != 3:
    print ('fin de intentos, no tuviste suerte')l
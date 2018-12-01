#!/usr/bin/python
cantidad = int(input('ingrese cantidad de cauchos a comprar: '))
i = 0
compra = 0
for i in range(cantidad):
    valor = int(input('ingrese el valor del caucho: '))
    compra = compra + valor
print ('total de la compra', compra)
descuento_mayor = compra*0.15
descuento_menor = compra*0.10
if cantidad >= 6:
    msge = ('al comprar mas de 6 se aplica descuento del 15% que es')(descuento_mayor) 
    print (msge)
    #print ('al comprar mas de 6 se aplica descuento del 15% que es', (descuento_mayor)+'el valor a pagar', compra-descuento_mayor)
else:
    print ('al comprar menos de 6 se aplica descuento del 10%, valor a pagar', compra-descuento_menor)

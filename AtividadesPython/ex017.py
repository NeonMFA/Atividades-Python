#Um Programa que Faça o Calculo da Hipotenusa 

from math import hypot

co = float(input('Qual o Cateto Oposto? '))
ca = float(input('Qual o Cateto Adjacente? '))
hi = hypot(ca, co)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

#Um Programa que Mostre a Parte Inteira de Um Número

import math

n1 = float(input ('Digite um número: '))
print('O numero {} tem {} como parte inteira'.format(n1, math.trunc(n1)))
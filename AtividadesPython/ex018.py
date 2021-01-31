#Um Programa que Calcule o Seno, Cosseno e Tangente do Angulo

import math

angle = float(input('Qual é o angulo?'))

an = math.radians(angle)
co = math.cos(an)
se = math.sin(an)
ta = math.tan(an)

print('O Seno do angulo é {:.2f}, o Cosseno é {:.2f}, e a Tangente é {:.2f}'.format(se, co, ta))

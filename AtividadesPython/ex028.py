#Utilizando Random, o Usuario tem que Advinhar o Número Randomizado

import random

print('Vou pensar em um número de 0 a 5, Tente Advinhar...')
ran = (random.randint(0, 5))
num = int(input('Qual número você acha que será? '))

if num == ran:
    print('Parabéns, você acertou')
else:
    print('Você perdeu, tente novamente')


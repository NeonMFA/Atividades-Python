#Um Programa que Randomize um Nome dos Inseridos

import random

n1 = str(input('Digite um nome:'))
n2 = str(input('Digite um segundo nome:'))
n3 = str(input('Digite um terceiro nome:'))
n4 = str(input('Digite um quarto nome:'))
lista = [n1, n2, n3, n4]
print('entre os alunos {} foi o escolhido'.format(random.choice(lista)))

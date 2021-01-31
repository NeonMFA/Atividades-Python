#O Mesmo jogo da advinhação, mas dessa vez pode inserir o valor muitas vezes e o programa só termina quando acertar o Valor

import random

bot = random.randrange(11)
res = 0
count = 0
while res != bot:
    res = int(input('Escolha um Número de 1 a 10: '))
    if res == bot:
        print('Você Acertou')
    elif res != bot:
        print('Tente Novamente')
    count += 1
print(f'Você precisou de {count} Tentativas')
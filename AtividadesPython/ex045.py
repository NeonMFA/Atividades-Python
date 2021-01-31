#Jogo de Pedra, Papel ou Tesoura

from random import randrange

print('Opções: \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')
esc = int(input('Escolha uma Opcão: '))
bot = randrange(3)
itens = ['Pedra', 'Papel', 'Tesoura']
print(f'O Jogador Jogou {(itens[esc])}')
print(f'O Computador Jogou {(itens[bot])}')
if bot == 0:
    if esc == 2:
        print('O Computador Ganhou')
    elif esc == 1:
        print('O Jogador Ganhou')
    else:
        print('Empate')
elif bot == 1:
    if esc == 2:
        print('O Jogador Ganhou')
    elif esc == 0:
        print('O Computador Ganhou')
    else:
        print('Empate')
elif bot == 2:
    if esc == 0:
        print('O Jogador Ganhou')
    elif esc == 1:
        print('O Computador Ganhou')
    else:
        print('Empate')

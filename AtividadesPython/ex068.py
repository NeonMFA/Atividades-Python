#Um jogo de Par Ou Impar

from random import randrange

count = 0
par = True
while True:
    num = int(input('Escolha um Número: '))
    escolha = str(input('Escolha Par ou Impar: [I/P] '))
    bot = randrange(1, 10)
    soma = num + bot
    print(f'A Maquina Escolheu {bot}, e a Soma foi {soma}')
    if soma % 2 == 0:
        par = True
    else:
        par = False
    if par and escolha == 'p' or par == False and escolha == 'i':
        print('Você Ganhou')
    else:
        print(f'Você Perdeu, e Ganhou {count} Vezes')
        break
    count += 1
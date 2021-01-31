#Mostra se Um Número é Primo ou Não

num = int(input('Escolha um Número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[34m', end=' ')
    else:
        print('\033[m', end=' ')
    print(c, end='')
print(f'\n\033[m0 Este número é divisivel por {tot} números')
if tot == 2:
    print('Por isso Este Número é um Número Primo')
else:
    print('Por isso Este Número Não é primo')



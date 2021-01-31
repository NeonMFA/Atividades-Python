#Você pode escolher qual operação realizar com os números escolhidos

num1 = float(input('Digite o Primeiro Número: '))
num2 = float(input('Digite o Segundo Número: '))
esc = 0
print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa')

while esc != 1 and esc != 2 and esc != 3 and esc != 5:
    esc = int(input('Escolha uma Opção: '))
    if esc == 1:
        print(f'A Soma entre eles é {num1 + num2}')
    elif esc == 2:
        print(f'A Multiplicação entre eles é {num1 * num2}')
    elif esc == 3:
        if num1 > num2:
            print('O Primeiro Número é Maior')
        elif num2 > num1:
            print('O Segundo Número é Maior')
    elif esc == 4:
        num1 = float(input('Digite o Primeiro Número Novamente: '))
        num2 = float(input('Digite o Segundo Número Novamente: '))
    elif esc == 5:
        print('Encerrando o Programa')
#Mostra um Sequencia de Números, Podendo escolher um Primeiro Termo e o Seu Passo. 
#Após Mostrar os 10 Primeiros Termos, o Usuario pode Escolher a Quantidade de Termos para Mostrar a Seguir.

termo = int(input('Insira o Primeiro Termo: '))
razão = int(input('Insira a Razão: '))
final = 10

while final != 0:
    final -= 1
    termo += razão
    print(termo)

while final != 20:
    final = int(input('Quantos Você quer mostrar a mais? '))
    while final != 0:
        final -= 1
        termo += razão
        print(termo)





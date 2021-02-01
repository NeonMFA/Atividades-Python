#Mostra uma sequencia de Números, Você pode escolher o Primeiro Termo, e o Passo

termo = int(input('Insira o Primeiro Termo: '))
razão = int(input('Insira a Razão: '))
final = 10
while final != 0:
    final -= 1
    termo += razão
    print(termo)
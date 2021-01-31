#Mostra Quantos Números Pares foram informados e a soma entre eles

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Coloque um Número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} Números Pares, e a Soma Entre Eles é {soma}')
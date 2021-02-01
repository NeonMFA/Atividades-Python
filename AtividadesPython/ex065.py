#Mostra a Media, o Maior Valor, e o Menor dos Números Digitados

num = 1
media = 0
maior = 0
menor = 0
count = 0
while not num == 0:
    num = int(input('Escreva um Número: [Digite 0 para Parar]: '))
    count += 1
    media += num
    if count == 1:
        menor = num
    elif num > maior:
        maior = num
    elif menor > num > 0:
        menor = num
print(f'Foram {count} Números, A Media foi {media / 2}, o Menor Valor foi {menor}, e o Maior foi {maior}')
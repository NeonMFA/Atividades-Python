#Mostra a Media, o Maior Valor, e o Menor dos Números Digitados

num = media = maior = menor = count = 0
resp = ''

while resp != 'n':
    num = int(input('Escreva um Número: [Digite 0 para Parar]: '))
    count += 1
    media += num
    resp = str(input('Você quer continuar? [S/N] '))
    if num > maior:
        maior = num
    if num < menor or count == 1:
        menor = num

print(f'foram {count} números, a media foi {media / count}, o menor foi {menor}, e o maior foi {maior}')

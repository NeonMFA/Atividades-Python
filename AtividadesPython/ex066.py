#Faz a Soma de Todos os Números e Quando for Colocado o Número 999, o programa acaba

soma = count = 0

while True:
    num = int(input('Escolha um Número: '))
    if num == 999:
        break
    count += 1
    soma += num

print(f'Você digitou {count} Números, e a Soma foi {soma}')
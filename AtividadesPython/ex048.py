#Mostra a soma de Número Impares Multiplos de 3

soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        soma += c
print(f'A soma de {count} Valores é igual a {soma}')

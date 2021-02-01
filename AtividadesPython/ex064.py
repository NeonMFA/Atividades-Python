#Soma a Quantidade de Valores Inseridos, Colocando 999 o Programa Para.

num = 0
soma = 0
count = 0
while not num == 999:
    num = int(input('Escreva Um Número:[Coloque 999 para Parar] '))
    soma += num
    count += 1
print(f'A Soma de {count - 1} Números foi {soma - 999}')
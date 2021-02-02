#Pergunta o Nome do Produto, o Preço, e se Quer Colocar Mais Valores
#No Final Mostra o Total Gasto, o Número de Produtos Maiores de 1000 e o Nome do Produto Mais Barato.

total = caro = barato = count = 0
nomebarato = ''

while True:
    name = str(input('Qual o Nome do Produto? '))
    price = float(input('Qual o Preço do Produto? '))
    opção = str(input('Você quer Continuar? [S/N] ')).lower()
    count += 1
    total += price
    if count == 1 or price < barato:
        barato = price
        nomebarato = name
    if price >= 1000:
        caro += 1
    if opção == 'n':
        break
print(f'o Total Gasto foi {total}, foram {caro} Produtos que Valem Mais que 1000 Reais, e o nome do mais barato foi o {nomebarato}')

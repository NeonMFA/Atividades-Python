#Mostra a Quantidade de Pessoas Maiores e Menores de Idade

from datetime import date

year = date.today().year
countnew = 0
countold = 0
for c in range(1, 8):
    nasc = int(input(f'Qual a Data de Nascimento da {c} Pessoa? '))
    yold = year - nasc
    if yold < 18:
        countnew += 1
    elif yold >= 18:
        countold += 1
print(f'Dessas Pessoas, {countnew} são Menores de Idade, e {countold} são Maiores de Idade')


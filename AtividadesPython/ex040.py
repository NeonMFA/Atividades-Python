#Mostra se está Aprovado, Reprovado, ou em Recuperação, utilizando a media de duas notas

n1 = float(input('Qual sua Primeira nota? '))
n2 = float(input('Qual sua Segunda Nota? '))
med = (n1 + n2) * 50/100
print(f'Tirando a nota {n1} e {n2}, você tera a média {med}')
if med >= 7:
    print('Aprovado')
elif 5 <= med < 6.9:
    print('Recuperação')
elif med < 5:
    print('Reprovado')
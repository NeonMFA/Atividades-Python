#Um Programa que Mostre a Área Utilizando a Largura e Altura Inserida

print('-'*100)
larg = float(input('Qual a largura em metros?'))
alt = float(input('Qual a altura em metros?'))
area = larg*alt
tinta = area/2
print('-'*100)
print('a área equivale a {}m² metros e a quantidade de tinta necessaria é {}l'.format(area, area/2))
print('-'*100)
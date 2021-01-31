#Um Programa que Coloca 5% de Desconto no Valor

n1 = float(input('Qual o preço?'))
print('o preço de {} ficara em'.format(n1), n1-(n1*5/100),'com 5% de desconto')
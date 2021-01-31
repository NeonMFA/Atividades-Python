#Um Programa que Transforme de Reais Para Dolar, Euro e Iene

print('-'*100)
d = float (input('Quantos Reais você tem em sua Carteira? '))
print('-'*100)
print('Valor do Dolar Americano: $5,05 \nValor do Euro: €6,11 \nValor do Iene: ¥0,049')
print('-'*100)
print('Conversão: \nReal: R${:.2f}  \nPara: \nDolar: ${:.2f} '.format(d, d/5.05) )
print('Euro: €{:.2f}'.format(d/6.11))
print('Iene: ¥{:.2f}'.format(d/0.049))
print('-'*100)
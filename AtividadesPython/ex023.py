#Analisa o Número, informando a Unidade, Dezena, Centena e Milhar

num1 = int(input('Informe um Número: '))
n = str(num1)
print(f'O Número a ser analisado é: {n}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
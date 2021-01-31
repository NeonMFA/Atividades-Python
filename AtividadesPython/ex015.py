#Um Programa que Calcule o Aluguel de Um Carro

dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro rodou? '))

print(f'o custo do aluguel é de R${(dia*60)+(km*0.15)}')

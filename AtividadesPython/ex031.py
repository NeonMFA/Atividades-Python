#Calcula o Preço por Km rodado de um Carro Alugado

km = float(input('Quantos Km você andou? '))
if km <= 200:
    print(f'Você terá que pagar {km*0.50:.2f}')
else:
    print(f'Você terá que pagar {km*0.45:.2f}')
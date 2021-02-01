#Mostra a Sequencia de Fibonacci

count = 2
term1 = 0
term2 = 1
num = int(input('Quantidade de Termos a Ser Mostrado: '))
print(f'{term1} ->', term2, end=' -> ')
while count != num:
    count += 1
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    print(term3, end= ' -> ')
print('Final')
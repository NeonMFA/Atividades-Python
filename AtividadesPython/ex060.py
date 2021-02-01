#Mostra o Factorial de um Número

from math import factorial

num = int(input('Escolha um Número: '))
count = num
while count != 1:
    count -= 1
    print(f'{count}', 'x' if count > 1 else ' = ',  end=' ')
print(factorial(num))

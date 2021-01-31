#Mostra o Primeiro Nome e o Ultimo

name = str(input('Qual o seu nome completo? ')).strip()
n1 = name.split()
print(f'o seu primeiro nome é {n1[0]}')
print(f'o seu ultimo nome é {n1[len(n1)-1]}')

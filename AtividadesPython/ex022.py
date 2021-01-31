#Mostra o Nome Inserido em Maiusculo, Minusculo, a Quantidade de Letras,e o Primeiro Nome e o Sobrenome

name = (input('Qual o seu nome? ')).strip()
print(f'seu nome em maiúsculo é {name.upper()}')
print(f'seu nome em minúsculo é {name.lower()}')
print(f'Seu nome tem ao todo {len(name )- name.count(" ")} Letras')
name2 = name.split()
print(f'Seu primeiro nome é {name2[0]} e tem {len(name2[0])} Letras')

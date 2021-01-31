#Mostra Qual foi o Maior Peso e o Menor

menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Qual O Peso da Pessoa {c}? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior > peso:
            maior = peso
        if menor < peso:
            menor = peso
print(f'O Menor foi {menor}Kg, e o Maior foi {maior}Kg')
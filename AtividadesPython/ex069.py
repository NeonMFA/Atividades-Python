#Insira a Idade, o Gênero e se Quer Inserir mais Valores. 
# Após isso Mostra o Número de Pessoas Maiores de 18, O Número de Homens e o Número de Mulheres com Menos de 20.

maior = homens = mulheres = 0

while True:
    idade = int(input('Escreva a Idade: '))
    genero = str(input('Escreva o Gênero: [M/F] ')).lower()
    escolha = str(input('Você Quer Continuar? [S/N] '))

    if idade >= 18:
        maior += 1
    if genero == 'm':
        homens += 1
    if genero == 'f' and idade < 20:
        mulheres += 1
    if escolha == 'n':
        break
print(f'foram {maior} maiores de 18, foram {homens} Homens, e foram {mulheres} Mulheres com menos de 20')

#Mostra a Media de Idade, a pessoa mais velha e o seu nome, e a quantidade de mulheres com menos de 17 anos

mediaidade = 0
maioridade = 0
maiorname = '0'
mulhermenor = 0
for p in range(1, 5):
    print(f'{p} Pessoa')
    name = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    gen = str(input('Genero[M/F]: ')).lower().strip()
    mediaidade += id
    if gen == 'f' and id < 20:
        mulhermenor += 1
    if p == 1:
        mediaidade = id
        menorname = name
    else:
        if maioridade < id:
            maioridade = id
            maiorname = name
print(f'A Media da Idade foi {mediaidade / 4} Anos')
print(f'A Pessoa Mais Velha tem {maioridade} e se chama {maiorname}')
print(f'Foram ao todo {mulhermenor} Mulheres Menores de 20 Anos')
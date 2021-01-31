#Um Programa que Mostra o Ano de Nascimento de Uma Pessoa e se ela pode se alistar, quantos anos falta para ela poder se alistar....

from datetime import date
nas = int(input('Ano de Nascimento: '))
data = date.today().year
idade = data - nas
print('Quem Nasceu em {} tem {} Anos em {}'.format(nas, idade, data))
if idade < 18:
    print(f'Ainda faltam {18 - idade} Anos para o alistamento')
    print(f'Seu alistamento será em {(18 - idade) + data}')
elif idade > 18:
    print(f'Já Deveria ter se Alistado há {idade - 18} Anos')
    print(f'O Seu Alistamento foi em {data - (idade - 18)}')
else:
    print('Você tem 18 Anos e Deve se Alistar')
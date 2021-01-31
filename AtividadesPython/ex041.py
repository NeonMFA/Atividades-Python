#Mostra Qual Categoria a Pessoa Está com Base na Sua Data de Nascimento

from datetime import date

year = int(input('Ano de Nascimento:'))
idade = date.today().year - year
print(f'Você tem {idade} Anos e Nasceu no em {year}')
if idade <= 9:
    print('Você é da Categoria Mirim')
elif idade <= 14:
    print('Você é da Categoria Infantil')
elif idade <= 19:
    print('Você é da Categoria Junior')
elif idade <= 25:
    print('Você é da Categoria Senior')
elif idade > 25:
    print('Você é da Categoria Master')

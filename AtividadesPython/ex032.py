#Um Programa pra Verificar se um Ano é Bissexto ou Não

from datetime import date

year = int(input('Escolha um ano para verificar se ele é Bissexto ou não: '))
if year == 0:
    year = date.today().year
    # if acima utilizado para ler o ano atual do computador utilizando o módulo importado.
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é Bissexto')
else:
    print(f'O ano {year} não é Bissexto')

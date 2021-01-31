#Mostra Qual Genero foi Escolhido e Caso Insira um Valor Invalido ira sempre Repetir a Pergunta

genre = 'a'
while genre != 'M' and genre != 'F':
    genre = str(input('Qual o Seu Gênero?[M/F] ')).upper().strip()
    if genre == 'M':
        print('Você escolheu o Gênero Masculino')
    elif genre == 'F':
        print('Você escolheu o Gênero Feminino')
    else:
        print('Tente Novamente')

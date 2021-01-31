#Mostra se é possivel fazer um Triangulo e Qual Triangulo é Formado

seg1 = float(input('Escolha o Primeiro Segmento: '))
seg2 = float(input('Escolha o Segundo Segmento: '))
seg3 = float(input('Escolha o Terceiro Segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('é Possivel formar um Triangulo')
    if seg1 == seg2 == seg3:
        print('é Possível fazer um Triangulo Equilátero')
    elif seg1 != seg2 != seg3 != seg1:
        print('é Possivel fazer um Triangulo Escaleno')
    else:
        print('é Possível fazer um Triangulo Isósceles')
else:
    print('Não é possivel formar um Triangulo')

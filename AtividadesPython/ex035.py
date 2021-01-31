#Programa que Verifica se é Possivel formar um Triangulo

n1 = float(input('Qual o Primero Segmento? '))
n2 = float(input('Qual o Segundo Segmento? '))
n3 = float(input('Qual o Terceiro Segmento? '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 +n2:
    print('É Possível Formar um Triangulo')
else:
    print('Não é Possivel Formar um Triangulo')
#Mostra a Tabuada do Número Inserido, caso utilize um Número Negativo o Programa Acaba 

count = 0
while True:
    if count == 0 or count == 10:
        num = int(input('Qual Tabuada Você quer? '))
        count = 0
    count += 1
    if num < 0:
        break

    print(f'{num} x {count} = {num * count}')
#Digite um Valor e Será Mostrado Quantas Cédulas Você Precisaria Sacar, Sendo Cédulas de 50, 20, 10 ou de 1.

num = int(input('Quanto Você Quer Sacar? '))
cedula = 50
total = num
count = 0
while True:
    if total >= cedula:
        total -= cedula
        count += 1
    else:
        print(f'Total de {count} Cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        count = 0
        if total == 0:
            break

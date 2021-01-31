#Um Programa Analisa a Velocidade Inserida, se for Maior que 80Km tera uma multa

vel = float(input('Qual a velocidade do seu carro? '))
multa = (vel-80)*7
if vel >80:
    print(f'Você Passou da Velocidade Permitida, Você foi multado em R${multa:.2f}!')
else:
    print('Você está na velocidade permitida, pode seguir em frente')
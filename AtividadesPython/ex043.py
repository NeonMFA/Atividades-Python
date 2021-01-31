#Calcula o Imc da Pessoa

peso = float(input('Qual o Seu Peso?(Kg) '))
alt = float(input('Qual a Sua Altura?(M) '))
imc = peso / (alt * alt)
print(f'seu IMC é {imc:.2f}')
if imc <= 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mordida')
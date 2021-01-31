#Conversão do Número inteiro para Binario, Octal, ou Hexadecimal

num = int(input('Escolha um Número Inteiro: '))
print('[1] para Binario \n[2] para Octal \n[3] para Hexadecimal')
met = int(input('Escolha Qual Será a Conversão: '))
if met == 1:
    print(bin(num)[2:])
elif met == 2:
    print(oct(num)[2:])
elif met == 3:
    print(hex(num)[2:])
else:
    print('Opção Invalida... Tente Novamente')
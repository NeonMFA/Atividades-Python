#Um Programa que Mostre Informações de Uma String

t1 = str(input('digite algo:'))
print('O tipo primitivo é', type(t1))
print('Só tem letras?', t1.isalpha())
print('Só tem letras minusculas?', t1.islower())
print('Tem letras e numeros?', t1.isalnum())
print('Só tem numeros?', t1.isnumeric())
print('Só tem letras maiusculas?', t1.isupper())

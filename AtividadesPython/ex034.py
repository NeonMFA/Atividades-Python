#Calcula o Aumento de Um Salario 

salario = float(input('Qual o seu Salário? '))
aumento = 0
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
   aumento = salario + (salario * 15 / 100)
print(f'O Salario de R$ {salario:.2f} teve um Aumento para R$ {aumento:.2f}')

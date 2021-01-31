#Um Programa que Aumente o Salario de uma Pessoa em 15%

salario = float(input ('Qual o salario do funcionario?'))
print(f'O Salario do funcionario é de {salario} e com um aumento de 15% será {salario+(salario*15/100):.2f}')
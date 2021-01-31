#Calcula se o emprestimo é liberado ou não, com base que o salario tem que ser maior que o minimo de 30% das parcelas

val = float(input('Qual o Valor da Casa? R$ '))
sal = float(input('Qual o Seu Salário? R$ '))
anos = int(input('Em Quanto anos você vai pagar? '))
pres = val / (anos * 12)
minimo = sal * 30/100
print(f'Para comprar uma casa de R$ {val:.2f}, você tera que pagar R$ {pres:.2f} por mês')
if pres <= minimo:
    print('Emprestimo Liberado')
else:
    print('Emprestimo Cancelado')
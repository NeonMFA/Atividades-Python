#Calcula Desconto ou Juros com Base na Escolha de Pagamento

price = float(input('Qual o Preço das Compras R$ '))
print('[1] Avista no Dinheiro/Cheque \n[2] Avista No Cartão \n[3] em até 2 vezes no Cartão \n[4] em 3 Vezes ou Mais')
met = int(input('Qual Metodo Você escolhe? '))

if met == 1:
    print(f'Sua Compra será a a vista no Dinheiro/Cheque, sua compra de R${price:.2f} saira por {(price - (price * 10/100)):.2f}')
elif met == 2:
    print(f'Sua compra será a vista no Cartão, sua compra de R${price:.2f} Saira por R${price - (price * 5/100):.2f}')
elif met == 3:
    print(f'Sua compra será feita em duas vezes no Cartão, por isso saíra por R${price:.2f}')
elif met == 4:
    par = int(input('Quantas Parcelas Você quer dividir? '))
    price2 = price + (price * 20/100)
    parc = price2 / par
    print(f'Sua compra de R${price:.2f} foi Parcelada em {par} vezes, por isso saíra por {price2:.2f} com parcelas de {parc:.2f} por mês')
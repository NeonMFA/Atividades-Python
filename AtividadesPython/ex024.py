#Mostra True ou False se o Nome da Cidade tem Santo
name = str(input('Qual o nome da sua cidade?')).strip()
print(name[:5].upper() == 'SANTO')
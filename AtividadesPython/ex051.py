#Mostra os 10 Primeiros Termos, Você escolhe o Primeiro termo e o passo

ter = int(input('Primeiro Termo: '))
rez = int(input('Razão: '))
endt = ter + 10 * rez
for c in range(ter, endt, rez):
    print(c, end=' -> ')
print('Acabou')
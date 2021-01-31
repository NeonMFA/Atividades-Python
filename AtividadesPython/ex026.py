#O Programa Analisa a letra A na Frase Inserida

f1 = str(input('Digite uma Frase: ')).lower().strip()
print(f'A Letra A Aparece {f1.count("a")} Vezes na Frase')
print(f'A Primeira Letra A apareceu na posição {f1.find("a")+1}')
print(f'A Ultima Letra A apareceu na posição {f1.rfind("a")+1}')

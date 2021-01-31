#Mostra se a Frase é um Palindromo ou Não

n1 = str(input('Digite Uma Frase: ' )).upper().strip()
word = n1.split()
n2 = ''.join(word)
rev = n2[::-1]
if n2 == rev:
    print('é um Palindromo')
else:
    print('Não é um Palindromo')
print(n2)
print(rev)
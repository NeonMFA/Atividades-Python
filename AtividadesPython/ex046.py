#Faz uma Contagem Regresiva de 10 a 1

from time import sleep

for count in range(10, -1, -1):
    sleep(1)
    print(count)
print('BUM!')


'''Exercício Python 46: Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
i = int(10)
f = int(0)
p = int(-1)

for c in range(i, f-1, p):
    print(c)
    sleep(1)

print('BOOOMM!!!')

''' ou pode ser feito desta forma:

for cont in range(10, -1, -1)
  print(cont)
  sleep(0.5)
print('boomm, boomm')
 



'''
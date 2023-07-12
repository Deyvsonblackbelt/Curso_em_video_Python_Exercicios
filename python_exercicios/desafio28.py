# Escreva um programa que faça o computador pensar em um número inteiro entre 0 a 5 e peça para o usuario
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuario
# venceu ou perdeu.

import random as rd
from time import sleep

resultado = rd.randint(0, 5)
print('-=-'*23)
print('vou sortear um número entre 0 e 5 tente advinhar qual foi o número! ')
print('-=-'*23)
n = int(input('Qual é o seu palpite? digite um número: '))
print('>>>PROCESSANDO<<<')
sleep(3)
print('')
if n == resultado:
    print('Parabéns voçê acertou ! venceu o desafio!')
else:
    print(f' infelizmente voçê perdeu o resultado do sorteio foi {resultado}!')


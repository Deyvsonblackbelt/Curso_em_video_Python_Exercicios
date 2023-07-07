# Crei um programa que leia na tela um número real qualquer pelo teclado
#e mostre na tela sua porção inteira  ex: 6,127 parte inteira é 6
import math

num = float(input('digite um número real: '))
pos = math.trunc(num)
print(pos)


'''todas tratam-se de funções que retornam apenas a parte inteira.
trunc = Retorna apenas a parte inteira do número, ignorando os decimais
ceil = Retorna apenas a parte inteira do número, arredondando para cima
floor = Retorna apenas a parte inteira do número, arredondado para baixo
Na prática, tendo como entrada o valor 1.9:
trunc = Retorna 1, pois ignora a parte decimal
ceil = Retorna 2, pois arredondou para cima
floor = Retorna 1, pois arredondou para baixo'''

# outra forma de fazer sem precisar de importar a biblioteca

outroNum = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(outroNum, int(outroNum)))
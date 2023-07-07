import math
import random
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num) # o metodo sqrt mostra a raiz quadrada do número.
print(f'A raiz de {num} é igual a {math.ceil(raiz)}') # metodo ceil faz o arredondamento do número. floor tem o efeito contrario.

numero = random.random()# gera um número aleatório
num_m = random.randint(1,10)# gera um número aleatório entre 1 e 10
print(numero)
print(num_m)

print(emoji.emojize('Olá mundo, emoji_type '))

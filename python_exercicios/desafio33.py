# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
# verificando quem é o menor

menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t

# verificando quem é o maior

maior = p
if s > p and s > t:
    menor = s
if t > p and t > s:
    menor = t

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

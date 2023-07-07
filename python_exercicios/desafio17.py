# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot
'''ca = float(input('Coloque o comprimento do cateto adjacente: '))
co = float(input('Coloque o comprimento do cateto oposto: '))
hi: float = (co**2 + ca**2)**(1/2)
print(f"A hipotenusa vai medir {hi:.2f}")'''

cad = float(input('digite o comprimento do cateto adjacente: '))
cao = float(input('digite o comprimento do catedo oposto: '))
hip = hypot(cad, cao)
print(f'O comprimento da hipotenusa é {hip:.2f}')
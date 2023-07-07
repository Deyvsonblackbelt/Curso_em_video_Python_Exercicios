# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule sua área e a quantidade de tinta necessária para
# pinta-lá, sabendo que cada litro de tinta, pinta uma areá de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
vari = 'x'
área = larg * alt
tinta = área / 2

print(f'Sua parede tem uma dimensão de {larg}m x {alt}m² e sua área é de {área}m² ')
print(f'para pintar essa parede voçê precisará de {tinta} litros de tinta!')
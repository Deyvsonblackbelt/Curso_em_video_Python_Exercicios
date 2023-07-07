# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
desconto = preco * 5
total = preco - desconto / 100

print(f'O produto que custava {preco}, na promoção com 5% de desconto vai custar R${total}')
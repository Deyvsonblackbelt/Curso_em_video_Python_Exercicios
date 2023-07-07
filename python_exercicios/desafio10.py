# crie um programa que mostre quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere uss1,00 = R$3,27

carteira = float(input('Quanto dinheiro voçê tem na carteira? R$ '))
dolar = carteira / 3.23

print(f'Com R${carteira:.2f} voçê pode comprar USS{dolar:.2f}')
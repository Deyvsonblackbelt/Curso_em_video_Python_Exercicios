# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

v = float(input('Qual foi a velocidade do carro? '))
m = (v - 80) * 7
if v >= 80:
    print(f'voçê ultrapassou o limite de velocidade de 80km/h sua multa por ultrapassar o limite é R${m:.2f}')
else:
    print('Voçê está dentro do limite de velocidade permitido!')
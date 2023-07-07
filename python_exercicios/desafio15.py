# Escreva um programa que pergunte a quantidade de km
# precorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input('Quantos KM foi percorrido pelo carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
dias_total = dias * 60
km_total = km * 0.15
total_pagar = dias_total + km_total

print(f'Voçê rodou {km}km com o carro por {dias} dias o valor total a ser pago é {total_pagar}')
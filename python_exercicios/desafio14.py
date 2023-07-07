# Escreva um programa que converta uma temperatura digitada
# em °C e converta para °F e °K.

c = float(input('Escreva a temperatura desejada: '))
f = c * 9 / 5 + 32
k = c + 273.15
print(f'A temperatura convertida para Farenheint é {f}°F')
print(f'E para graus Kelvin é {k}°K')
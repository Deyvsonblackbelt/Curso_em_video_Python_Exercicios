# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input('Digite um número de 0 a 9999: '))

print(f'''
Unidade: {num%10}
Dezena: {(num//10)%10}
Centena: {(num//100)%10}
Milhar: {(num//1000)%10}

''')

num2 = str(input('Digite outro número de 0 a 9999: '))
print(f'''
Unidade: {num2[3]}
Dezena: {num2[2]}
Centena: {num2[1]}
Milhar: {num2[0]}

''')
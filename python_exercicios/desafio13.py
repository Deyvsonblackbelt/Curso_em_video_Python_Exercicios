# Faça um programa que leia o sálario de um funcionário
# e mostre seu novo sálario, com 15% de aumento.

salario = float(input('Digite o seu salário: '))
aumento = salario * 15 / 100 + salario

print(f'Seu novo salário com 15% de aumento é R${aumento}')
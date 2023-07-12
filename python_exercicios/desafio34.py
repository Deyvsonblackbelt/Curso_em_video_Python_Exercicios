# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Quanto é o seu salario atual: '))
if sal >= 1250:
    soma =sal + (sal * 10/100)
    aum = (sal * 10/100)
    print(f'Seu salário teve um aumento de R${soma:.2f} seu novo salário é R${aum:.2f} ')

if sal < 1250:
    somaa = sal + (sal * 15)/100
    aumen = (sal * 15)/100
    print(f'Seu salário teve um aumento de R${aumen:.2f} seu novo salário é R${somaa:.2f}')
# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Quanto é o seu \33[;32;40msalario atual\33[m: '))
if sal >= 1250:
    soma =sal + (sal * 10/100)
    aum = (sal * 10/100)
    print(f'Seu salário teve um aumento de R${aum:.2f} seu novo salário é R${soma:.2f} ')

if sal < 1250:
    somaa = sal + (sal * 15)/100
    aumen = (sal * 15)/100
    print(f'Seu salário teve um aumento de \33[;32;40mR${aumen:.2f}\33[m seu novo salário é \33[;32;40R${somaa:.2f}\33[m')
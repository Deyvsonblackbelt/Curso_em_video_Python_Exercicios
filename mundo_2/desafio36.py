"""
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
      o salário do comprador e em quantos anos ele vai pagar.
      A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
"""

casa = float(input('Qual o valor da casa desejar financiar? '))
sal = float(input('Qual é a sua renda mensal? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestação = casa / (anos * 12)
minimo = sal * 30/100

if minimo <= prestação:
    print(f'Para pagar uma casa de {casa:.2f} em {anos} anos a prestação será de {prestação:.2f}  ')
    print('Seu empréstimo não foi aprovado!')
else:
    print('Seu empréstimo foi aprovado!')
    print(f'a mensalidade da casa será de R${prestação:.2f}')

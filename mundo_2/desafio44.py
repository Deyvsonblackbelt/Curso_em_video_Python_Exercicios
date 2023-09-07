'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJAS MELO'))
produto = float(input('Qual o valor do produto? R$ '))
pagamento = input('''Escolha a forma de pagamento digitando o numero correspondente: 
                  [ 1 ] - À vista dinheiro/cheque 
                  [ 2 ] - À vista no cartão 
                  [ 3 ] - Em até 2x no cartão 
                  [ 4 ] - 3x ou mais no cartão   
                    ''')

if pagamento == '1':
    print(f'O valor final do produto é R${produto - produto*0.10} com 10% de desconto!')

elif pagamento == '2':
    print(f'O valor final do produto é R${produto - produto*0.05} com 5% de desconto!')

elif pagamento == '3':
    print(f'O valor do produto ficará em R${produto}!')
    print(f'O valor da parcela em 2x é R${produto/2}')

elif pagamento == '4':
    total = produto + (produto * 20/100)
    parcela = int(input("Em quatas vezes quer dividir? "))
    print(f'O valor final do produto é R${total} com 20% de juros!')
    print(f'O valor da parcela em {parcela}x é R${total/parcela} ')

else:
    print('Opção invalida !')
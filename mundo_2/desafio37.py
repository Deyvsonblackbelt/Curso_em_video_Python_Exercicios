# escreva um programa que leia um número inteiro e peça
# para o usuário escolher qual será a base de conversão.
# - 1 para biário, -2 para octal, 3 para hexadecimal.
while True:
    num = str(input('Digite um número inteiro: '))
    base = int(input('''
       Escolha uma dessas bases para conversão: 
       [ 1 ] Converter para BINÁRIO
       [ 2 ] Converter para OCTAL
       [ 3 ] Converter para HEXADECIMAL 
       [ x ] Sair 
    '''))
    print(f'Sua opção: {base}')
    if base == 'x' or base == 'X':
        break

    if base == 1:
        print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')

    elif base == 2:
        print(f'{num} convertido para OCTAL é igual a {oct(num)}')

    elif base == 3:
        print(f'{num} convertido para HEXADECIMAL é igual a{hex(num)}')

    else:
        print('Opção invalida!')
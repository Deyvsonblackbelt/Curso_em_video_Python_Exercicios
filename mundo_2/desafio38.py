# Escreva um programa que leia dois números inteiros
# e compare-os mostrando na tela a seguinte mensagem:
# 1 o primeiro valor é maior , o segundo valor é maior, não existe
# valor maior os dois são iguais.

num_um = int(input('Primeiro número: '))
num_dois = int(input('Segundo número: '))

if num_um > num_dois :
    print('O PRIMEIRO valor é maior!')

elif num_dois > num_um:
    print('O SEGUNDO valor é maior')

elif num_um == num_dois or num_dois == num_um:
    print('Não existe valor maior os dois são iguais!')

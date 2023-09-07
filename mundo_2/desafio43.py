'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))

imc = peso / (altura ** 2)
print(f'imc {imc:.2f}')
if imc < 18.5:
    print('Você está \33[;49;32mABAIXO DO PESO!\33[m ')

elif 18.5 <= imc < 25:
    print('Você está no \33[;49;34mPESO IDEAL!\33[m')

elif 25 <= imc < 30:
    print('Você está com \33[;49;33mOBESO!\33[m')

elif 30 <= imc < 40:
    print('Você está com \33[0;49;35mOBESIDADE!\33[m')

else:
     print('cuidado você está com \33[;49;31mOBESIDADE MÓRBIDA\33[m')

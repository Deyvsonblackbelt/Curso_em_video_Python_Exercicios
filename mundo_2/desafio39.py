# faça um programa que leia o ano de nascimento de um jovem e
# informe de acordo com sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora de se alistar ou se já passou do tempo de alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou o prazo do
# prazo.

from datetime import date

nasci = int(input('Ano de nascimento: '))
base = date.today().year
idade = base - nasci
if base - nasci == 18:
    print(f'Já tem {idade} anos a idade certa pra se alistar!')

elif base - nasci < 18:
    print('Ainda não tem idade suficiente para o alistamento')
    if base - nasci < 18:
        saldo = 18 - idade
        print(f'Ainda falta {saldo} anos!')
        ano = base + saldo
        print(f'Seu alistamento será em {ano}. !')

elif base - nasci > 18:
    saldo = idade - 18
    print(f'Voçe já passou da idade de se alistar! pois tem {saldo} anos a mais da idade de alistamento ')
    ano = base - saldo
    print(f'Você já deveria ter se alistado no de {ano}.')


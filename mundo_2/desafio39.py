# faça um programa que leia o ano de nascimento de um jovem e
# informe de acordo com sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora de se alistar ou se já passou do tempo de alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou o prazo do
# prazo.


ano = int(input('Ano de nascimento: '))
base = 2023
cal = base - ano
if base - ano == 18:
    print(f'Já tem {cal} anos a idade certa pra se alistar!')

elif base - ano < 18:
    print('Ainda não tem idade suficiente para se alistar')
    if base - ano < 18:
        print(f'Ainda falta {18-cal} anos!')

elif base - ano > 18:
    print(f'Voçe já passou da idade de se alistar! pois tem {cal-18} anos a mais da idade de alistamento ')


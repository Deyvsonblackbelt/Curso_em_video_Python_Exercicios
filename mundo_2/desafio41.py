#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:

'''– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date

nascimento = int(input('Ano de nascimento '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos!')
    print('Classificação: \33[;49;37mMIRIM\33[m!')

elif 15 > idade > 9:
    print(f'O atleta tem {idade} anos!')
    print('Classificação: \33[;49;33mINFANTIL\33[m!')

elif 20 > idade > 14:
    print(f'O atleta tem {idade} anos!')
    print('Classificação: \33[;49;31mJUNIOR\33[m!')

elif 26 > idade > 19:
    print(f'O atleta tem {idade} anos!')
    print('Classificação: \33[;49;35mSÊNIOR\33[m!')

else:
    print(f'O atleta tem {idade} anos!')
    print('Classificação: \33[;49;36mMaster\33[m!')

# também pode ser feito da seguinte forma " elif idade <=14: para todos os elifs "
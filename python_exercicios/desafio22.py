''' Crie um programa que leia o nome completo de uma pessoa e mostre:
 o nome com todas as letras maisculas.
 o nome com todas as letras minusculas.
 quantas letras ao todo sem considerar os espaços.
 quantas letras tem o primeiro nome.
 '''

nome = input('Digite o seu nome completo: ').strip()# metodo strip vai eliminar os espaços em branco da esq. e dire...
sem_espacos = ''.join(nome.split())
primeiroNome = nome.split()
print(f''' 
seu nome com todas as letras maiusculas {nome.upper()}
seu nome com todas as letras minusculas {nome.lower()}
quantidades total das letras do nome {len(sem_espacos)}# ou len(nome) - nome.count(' ')
quantidades de letras só do primeiro nome {len(primeiroNome[0])}# ou nome.find(' ')
''')


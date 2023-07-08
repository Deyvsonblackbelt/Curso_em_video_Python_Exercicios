# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().title()
sep = nome.split()
first = sep[0]
last = sep[-1]
print(f'''
Seu primeiro nome é {first}! 
Seu ultimo nome é {last}!
''')
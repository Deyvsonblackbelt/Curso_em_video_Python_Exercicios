# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite a cidade de onde voçê nasceu: ').strip().lower()
print('santo' in cidade[:5]) # ou cidade[:5] == 'santo'
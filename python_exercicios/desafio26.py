# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra 'a' em que posição ela
#aparece pela primeira vez e em que posição ela aparece pela ultima vez.

palavra = input('Digite uma frase qualquer: ').strip().lower()
quantidade = palavra.count('a')
print(f'''
Quantidade de vezes que a letra "a" aparece na frase é {quantidade} vezes!
A primeira vez que a letra "a" aparece na frase é na posição {palavra.find('a')+1} # mais um porque o python conta começando do zero.
A ultima vez que a letra "a" aparece na frase é na posição {palavra.rfind('a')+1}
''')
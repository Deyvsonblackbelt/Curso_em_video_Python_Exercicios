# Um professor que sortear um de seus quatro alunos para apagar
# o quadro. faça um programa que ajude ele, lendo o nome deles
# e escrenvendo o nome escolhido.

from random import choice
lista1 = []
prim = str(input(' Primerio aluno: '))
sec = str(input(' Segundo aluno: '))
ter = str(input(' Terceiro aluno: '))
quar = str(input(' Quarto aluno: '))

lista1.append(prim)
lista1.append(sec)
lista1.append(ter)
lista1.append(quar)
sort = choice(lista1)

print(f'O aluno escolhido foi {sort} ')
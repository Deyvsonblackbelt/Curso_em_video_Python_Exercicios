# O mesmo professor do desafio anterior quer sortear a ordem
#de apresentação de trabalhos dos alunos. Faça um programa que leia
#o nome dos quatros alunos e mostre a ordem sorteada.


from random import shuffle
lista1 = []
prim = str(input(' Primerio aluno: '))
sec = str(input(' Segundo aluno: '))
ter = str(input(' Terceiro aluno: '))
quar = str(input(' Quarto aluno: '))

lista1.append(prim)
lista1.append(sec)
lista1.append(ter)
lista1.append(quar)

shuffle(lista1)

print(f'A ordem de apresentação será: {lista1} ')
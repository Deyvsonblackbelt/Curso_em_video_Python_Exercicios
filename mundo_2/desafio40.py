# Crie um programa que leia duas notas de um aluno e calcule sua media.
# mostrando uma mensagem no final, de acordo com a média atingida.
# - média abaixo de 5.0: REPROVADO, - média entre 5,0 e 6,9: RECUPERAÇÃO
# - média 7.0 ou superior: APROVADO.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média foi {media} infelizmente você foi \33[;49;31mREPROVADO\33[m!')

elif media >= 7.0:
    print(f'Sua média foi {media} Parabéns voi foi \33[;49;34mAPROVADO\33[m!')

elif 7 > media >= 5:
    print(f'Sua média foi {media} voçê está em \33[;49;33mRECUPERAÇÃO\33[m! estude mais!')
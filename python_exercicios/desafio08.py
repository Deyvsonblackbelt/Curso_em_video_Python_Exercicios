# escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

metros = float(input('digite um valor em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 10 * 10
ml = metros * 10 * 10 * 10


print(f'A medida de {metros}m corresponde a :')
print(f'{km:.2f}km,  \n{hm:.2f}hm, \n{dam:.2f}dam,  \n{dm:.2f}dm, \n{cm:.2f}cm , \n{ml:.2f}ml,')
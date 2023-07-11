nome = str(input('Qual é o seu nome? ')).title().strip()
if nome == 'Deyvson':
    print('Que nome lindo voçê tem!')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}!')

n1_1 = str(input('Digite a primeira nota: ')).replace(',', '.')
n2_2 = str(input('Digite a segunda nota: ')).replace(',', '.')
n1 = float(n1_1)
n2 = float(n2_2)

m = (n1+n2)/2

print(f'A sua média foi {m:.2f}')
if m >= 6:
    print('Sua média foi boa "PARABÉNS"!')
else:
    print('Sua média não foi boa "ESTUDE MAIS"!')
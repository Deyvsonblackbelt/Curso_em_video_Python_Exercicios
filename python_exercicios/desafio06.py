# crie um programa que o usuario vai digitar um número e mostrara na tela o dobro o triplo e a raiz quadarada desse número.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f'''
         O dobro do número digitado é {dobro} !
         O triplo do número digitado é {triplo} !
         A raiz quadrada do número digitado é {raiz:.2f} ! 
''')

# pow(num,(1/2) tambem calcula a raiz quadrada!
# Faça um programa que leia algo pelo teclado
# e mostre na tela seu tipo primitivo e todas as informações possíveis

tipos = input('digite algo: ')

print(f''' O tipo primitivo desse valor é {type(tipos)} 
           Só tem espaços ? {tipos.isspace()}
           É alfalbético ?   {tipos.isalpha()}           
           É númerico ? {tipos.isnumeric()}
           É númerico e alfabético ? {tipos.isalnum()} 
           Só tem letras maiusculas ? {tipos.isupper()}
           Só tem letras minusculas ? {tipos.islower()}
           Está capitalizada ? {tipos.istitle()}
''')
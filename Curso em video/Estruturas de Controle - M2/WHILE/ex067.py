"""
EXERCÍCIO 067: Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

print(30*'~')
print('TABUADA DE QUALQUER NÚMERO')
print(30*'~')

while True:
    numero = int(input('Qual a tabuada que você quer saber [NEGATIVO SAI DO PROGRAMA] ? '))
    if numero < 0: 
        break
    print(30*'~')
    for i in range(0, 11):
        print(f'{i} x {numero} = {numero*i}')
    print(30*'~')

print('''
PROGRAMA FINALIZADO''')
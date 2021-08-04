"""
EXERCÍCIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input('Digite um número: '))
tot = 0
for seq in range(1, num + 1):
    if num % seq == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{seq} ', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso, ele É PRIMO!')
else:
    print('E por isso, ele NÃO É PRIMO!')
    
"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('Saber a PA de qualquer número com qualquer razão.')
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = prim + ((10 - 1) * raz)

for seq in range(prim, decimo + raz, raz):
    print(f'{seq} ')
print('ACABOU')
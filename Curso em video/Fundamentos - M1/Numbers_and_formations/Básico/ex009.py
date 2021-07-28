"""
EXERCÍCIO 009: Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
numero = float(input('Digite um número que queira saber a tabuada: '))

print(f'* Tabuada do {numero} *')
print(18*'-')
for i in range(0,11):
    print(f'{numero:.2f} x {i} = {numero*i:.2f}')
print(18*'-')
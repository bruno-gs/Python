"""
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

num = int(input('Digite um número para conferir: '))
cond = num % 2 == 0
if cond:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')
    
"""
EXERCÍCIO 074: Maior e Menor Valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""

from random import randint

numeros = ()
for i in range(5):
    numeros += (randint(1,10),)

print('Os números gerados aleatoriamente foram: ')
print(numeros)

print(f'\nO maior: {max(numeros)}')
print(f'O menor: {min(numeros)}')

"""
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O primeiro é maior.')
elif num1 < num2:
    print('O segundo é maior')
else:
    print('São iguais')

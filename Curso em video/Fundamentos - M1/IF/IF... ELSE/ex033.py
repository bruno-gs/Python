"""
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um outro número: '))
num3 = float(input('Digite um terceiro número: '))

maior = num1
menor = num1
if num2 > maior:
    maior = num2
else:
    menor = num2

if num3 > maior:
    maior = num3
else:
    if num3 < menor:
        menor = num3

print(f'O maior digitado foi {maior}')
print(f'O menor digitado foi {menor}')
"""
EXERCÍCIO 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
atual = date.today().year

maior = 0
menor = 0

for cd in range(7):
    ano = int(input('Qual o ano do seu nascimento? '))
    idade = atual - ano
    if idade >= 21:
        maior +=1
    else:
        menor +=1

print(f'Temos no total: {menor} pessoas menores e {maior} maiores de 21 anos.')

"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 5,11 (28/07/2021)
"""

valor = float(input('Diga-me quando reais possui na carteira: '))
dolar = 5.11
conversao = valor / dolar

print(f'Com R${valor:.2f}, no valor para cada dólar de R${dolar:.2f}, você poderia comprar U${conversao:.2f}')
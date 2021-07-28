"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

prateleira = float(input('Coloque o valor do produto na prateleira: R$'))
desconto = 0.05
print(f'Com {desconto*100}% de desconto, o novo valor será de R${(prateleira*(1-desconto)):.2f}')

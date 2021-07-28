"""
EXERCÍCIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

rodagem = float(input('Informe a km percorrida: '))
dias = int(input('Informe por quantos dias o carro ficou alugado: '))
custo = ((dias * 60) + (rodagem * 0.15))
print(f'Para {dias} dias e com {rodagem:.2f} km rodados, sua fatura é de R${custo:.2f}')

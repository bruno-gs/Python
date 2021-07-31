
"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

print('Aprovador de Empréstimo')
casa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
tempo = int(input('Digite em quantos anos deseja pagar: '))

mensal = casa / (tempo*12)
limite = 0.3 * salario

if limite >= mensal:
    print('Iremos continuar a negociação do empréstimo.')
else:
    print('Empréstimo negado.')

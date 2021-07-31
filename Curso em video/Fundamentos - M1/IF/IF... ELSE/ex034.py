"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Digite seu salario atual: R$'))
cond = salario > 1250
if cond:
    print(f'Seu novo salário será de R${salario * 1.10:.2f}')
else:
    print(f'Seu novo salário será de R${salario * 1.15:.2f}')
"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Digite seu salário: R$'))
aumento = 0.15
print(f'''Devido a sua evolução e dedicaçaõ na TCS, você terá um aumento de {aumento*100:.2f}%.
O seu novo salário será de R${(salario*(1+aumento)):.2f}''')

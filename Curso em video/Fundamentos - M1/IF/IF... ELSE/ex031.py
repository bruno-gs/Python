"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""
viagem = int(input('Digite a distância da viagem (em km): '))
cond = viagem <= 200
if cond: 
    print(f'O valor da passagem será de R${0.5*viagem:.2f}')
else:
    print(f'O valor da passagem será de R${0.45*viagem:.2f}')

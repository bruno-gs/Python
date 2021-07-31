"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

veloc=float(input('Digite a velocidade do veículo (em km/h): '))
verif = 80 < veloc
dif = -(80 - veloc)
if verif:
    print(f'Você foi multado! Pague R${dif *7:.2f}')
else:
    print(f'Você NÃO foi multado! Estava a {-dif}km/h abaixo do limite.')
"""
EXERCÍCIO 091: Jogo de Dados em Python

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
    Guarde esses resultados em um dicionário. 

No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
ranking = dict()

print('VALORES SORTEADOS:')

for i in range(1, 5):
    valor = randint(1, 6)
    jogadas[f'Jogador_{i}'] = valor

    print(f'Jogador_{i} tirou {valor} no dado.')

    sleep(1)

print('-=' * 15)
print('== RANKING DOS JOGADORES ==')

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
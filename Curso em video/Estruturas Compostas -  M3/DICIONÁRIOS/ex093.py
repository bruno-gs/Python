"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol

Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
    O programa vai ler o nome do jogador e quantas partidas ele jogou. 
    
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador                 = dict()
jogador['Nome']         = input('Nome: ')
partidas                = int(input(f'Quantas partidas o {jogador["Nome"]} jogou?: '))

total_gols = 0

for rodadas in range(1, partidas+1):
    jogador[f'Partida_{rodadas}'] = int(input(f'Quantos gols na partida {rodadas}? '))
    total_gols += jogador[f'Partida_{rodadas}']

# print(jogador)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas pelo Santos FC\n \
        Marcando {total_gols} gols.')

print(20*'=')
for rodadas in range(1, partidas+1):
    for k, v in jogador.items():
        t = f'Partida_{str(rodadas)}'
        if k == t:
            print(f' - Na rodada {rodadas} marcou {v} gols')
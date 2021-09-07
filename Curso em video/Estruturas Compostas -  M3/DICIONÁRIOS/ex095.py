"""
EXERCÍCIO 095: Aprimorando os Dicionários

Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partida.clear()
    for i in range(1, tot + 1):
        partida.append(int(input(f'    Quantos gols na partida {i}? ')))
    jogador['Gols'] = partida[:]
    jogador['Total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Somente S ou N.')
    if resp in 'N':
        break
print('-='*30)
print(f'cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"].upper()}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

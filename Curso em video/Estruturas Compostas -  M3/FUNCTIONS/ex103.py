def ficha(nome='<desconhecido>', gol=0):
    print(f'O {nome} fez {gol} gol(s) no campeonato!')


n = str(input('Jogador: '))
g = str(input('Quantos gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

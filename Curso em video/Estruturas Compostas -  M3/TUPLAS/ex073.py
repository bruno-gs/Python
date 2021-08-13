"""
EXERCÍCIO 073: Tuplas com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Utilizado de 2021, rodada 15.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""

campeonato = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino', 'Flamengo','Athletico-PR','Ceará','Santos','Atlético-GO',
'Bahia','Inter','Corinthians','Fluminense','Juventude','Sport','São Paulo','América-MG','Cuiabá','Grêmio','Chapecoense')

print('='*40)
print('Tabela do Brasileirão 2021 na rodada 15: ')
print('='*40)
for posicao, time in enumerate(campeonato):
    print(f'{posicao +1}. {time}') 
print('='*40)

print('''Os 5 primeiros do campeonato Brasileiro de 2021 na rodada 15 são: 
''')
for posicao, time in enumerate(campeonato[0:5]):
    print(f'{posicao +1}. {time}') 
print('='*40)

print('''Os times na zona de rebaixamento no Brasileirão 2021 na rodada 15 são: 
''')
for posicao, time in enumerate(campeonato[16:]):
    print(f'{posicao +17}. {time}') 
print('='*40)

print('''Em ordem alfabética, temos: 
''')
for posicao, time in enumerate(sorted(campeonato)):
    print(f'{time}') 
print('='*40)

print(f'A posição do clube Chapecoense é o {campeonato.index("Chapecoense")+1} lugar')
print('=' * 40)

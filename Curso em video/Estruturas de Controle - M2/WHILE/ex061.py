"""
EXERCÍCIO 061: Progressão Aritmética v2.0

Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

prim_termo = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
var = 1
tot = prim_termo
print('PA: ',end='')
while var <= 10:
    print(f'{tot} -- ', end='')
    tot += raz
    var +=1
print('FIM')
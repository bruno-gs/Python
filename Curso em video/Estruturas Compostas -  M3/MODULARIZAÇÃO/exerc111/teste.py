from exerc111.utilidadescev import moeda
from exerc111.utilidadescev import dado


p = float(input('Digite o preço: R$'))
ti = float(input('Digite a porcentagem de incremento: '))
td = float(input('Digite a porcentagem de decremento: '))

moeda.resumo(p, ti, td)

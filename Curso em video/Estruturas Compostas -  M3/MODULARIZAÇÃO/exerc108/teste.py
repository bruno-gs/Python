from exerc108 import moeda

print('-=' * 30)
p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Descontando 15%, temos {moeda.moeda(moeda.diminuir(p, 15))}')
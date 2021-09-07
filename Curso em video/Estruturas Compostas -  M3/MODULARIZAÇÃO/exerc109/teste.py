from exerc109 import moeda

print('-=' * 30)
p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Descontando 15%, temos {moeda.diminuir(p, 15, True)}')
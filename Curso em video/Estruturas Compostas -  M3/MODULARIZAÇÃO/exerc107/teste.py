from exerc107 import moeda

print('-=' * 30)
p = float(input('Digite o preço: R$'))
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Descontando 15%, temos R${moeda.diminuir(p, 15)}')
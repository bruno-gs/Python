"""
EXERCÍCIO 070: Estatísticas em Produtos

Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

print('Estatísticas em Produtos')
print(30*'~')

total = caros = barato = aux = 0 
barato_nome = ''

while True:
    aux += 1
    produto = str(input(f'Digite o nome do produto {aux}: '))
    valor = float(input('Digite seu preço: '))
    
    total += valor

    if aux == 1 or valor < barato:
        barato = valor
        barato_nome = produto
    
    if valor > 1000:
        caros += 1

    print(30*'~')
    cond = str(input('Deseja continuar adicionando? [S/N] ')).strip().lower()    
    print(30*'~')
    if cond == 'n':
        break

print(f'Foram digitados {aux} produtos, resultando em R${total:.2f}')
print(f'{caros} produtos custam mais de R$1000,00')
print(f'O produto mais barato é o {barato_nome}, custando R${barato:.2f}')

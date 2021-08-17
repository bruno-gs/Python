"""
EXERCÍCIO 081: Extraindo Dados de uma Lista

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

print('\nExtraindo Dados de uma Lista\n')

dados = []

while True:
    num = int(input('Digite um valor: '))
    dados.append(num)
    
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if op in 'N':
        print('\nFinalizando...\n')
        break

print(f'\nForam digitados {len(dados)} números')

dados.sort(reverse=True)
print(f'Eles foram organizados em ordem decrescente: \n{dados}')
if 5 in dados:
    print('\nO número 5 está presente na lista')

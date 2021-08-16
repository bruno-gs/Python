"""
EXERCÍCIO 078: Maior e Menor Valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

print(30*'=')
print('Maior e Menor Valores na Lista')
print(30*'=')
print('Digite 5 números e sairá o maior e menor deles. \nAlém das posições que foram preenchidos.')
print(55*'~')
numeros = []

for pos in range(1,6):
    num = int(input(f'Digite o {pos} número: '))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

pos_maior = numeros.index(maior)
pos_menor = numeros.index(menor)

print(55*'^')
print(f'O maior número digitado foi o {maior}, na posição {pos_maior+1}')
print(f'O menor número digitado foi o {menor}, na posição {pos_menor+1}')

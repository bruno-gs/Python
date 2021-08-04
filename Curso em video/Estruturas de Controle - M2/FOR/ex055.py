"""
EXERCÍCIO 055: Maior e Menor da Sequência

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

print('Encontrando o maior e o menor peso')
for v in range(5):
    peso = float(input('Digite seu peso (em kg): '))
    if v == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O menor entre os pesos foi {menor} kg e o maior foi {maior} kg')
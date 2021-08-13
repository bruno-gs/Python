"""
EXERCÍCIO 075: Análise de Dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numeros = ()
for num in range(4):
    numeros += (int(input(f'Digite o {num+1} numero: ')), )

print(f'Os valores digitados foram: {numeros}')
print(f'\nO número 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na posição {numeros.index(3)+1}.')
else:
    print('Não há ocorrências de número 3')

for pos, valor in enumerate(numeros):
    if valor % 2 == 0:
        print(f'O número {valor}, na posição {pos +1} é par.')

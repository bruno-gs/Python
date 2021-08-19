"""
EXERCÍCIO 086: Matriz em Python

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[],[],[]]
for linha in range(0,3):
   for coluna in range(0,3):
      numero = int(input(f'Digite um valor para a posição ({linha}, {coluna}): '))
      matriz[linha].append(numero)


print(matriz[0])
print(matriz[1])
print(matriz[2])

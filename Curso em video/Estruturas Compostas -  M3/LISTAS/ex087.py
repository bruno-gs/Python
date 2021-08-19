"""
EXERCÍCIO 087: Mais Sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""


matriz = [[],[],[]]
par = 0
terc_col_soma = 0
seg_col_maior = 0
for linha in range(0,3):
   for coluna in range(0,3):
      numero = int(input(f'Digite um valor para a posição ({linha}, {coluna}): '))
      matriz[linha].append(numero)
      if numero % 2 == 0:
         par += numero
      if coluna == 2:
         terc_col_soma += numero
      if coluna == 1:
         if linha == 0:
            seg_col_maior = numero
         else:
            if numero > seg_col_maior:
               seg_col_maior = numero


print(matriz[0])
print(matriz[1])
print(matriz[2])

print('='*30)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da 3° coluna é {terc_col_soma}.')
print(f'O maior valor da segunda linha é {seg_col_maior}.')
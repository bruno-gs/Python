"""
EXERCÍCIO 007: Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

p_nota = float(input('Digite a nota da P1: '))
s_nota = float(input('Digite a nota da P2: '))

media = (p_nota+s_nota) / 2 

print(f'A média entre {p_nota:.2f} e {s_nota:.2f} é {media:.2f}')
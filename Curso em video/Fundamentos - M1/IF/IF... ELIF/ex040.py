"""
EXERCÍCIO 040: Aquele Clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))

media = (p1 + p2) / 2

if media < 5: 
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!')
else:
    print('Recuperação')
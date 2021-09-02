"""
EXERCÍCIO 090: Dicionário em Python

Faça um programa que leia nome e média de um aluno, 
    guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}


aluno['nome']   = str(input('Nome: '))
aluno['media']  = float(input('Média: '))
if aluno['media']<5:
    aluno['situação'] = 'REPROVADO'
elif aluno['media'] > 7 :
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'    - {k} é igual a {v}')

'''
- nome é igual a BRUNO
- media é igual a 8.0
- situação é igual a APROVADO
'''

"""
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
from datetime import date
ano = int(input('Digite um ano para conferir (Coloque 0 para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year

bissexto = ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0
if bissexto:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é bissexto')

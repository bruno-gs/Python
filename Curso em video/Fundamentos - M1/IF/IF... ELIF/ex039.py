"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
hoje = date.today().year
nasc = int(input('Me conte seu ano de nascimento: '))

idade = hoje - nasc

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE.')
elif idade < 18:
    print(f'Você ainda terá que se alistar, faltam {18 - idade} anos para isso.')
else:
    print(f'Seu tempo de alistamento ja passou, aconteceu em {idade - 18} anos atrás.')
"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

metros = float(input('Me diga a medida em metros: '))
cent = metros*100
mil = metros * 1000

print(f'Seu valor é correspondente a {cent} centímetros ou {mil} milímetros')
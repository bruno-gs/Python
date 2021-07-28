"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot
cat_o = float(input('Comprimento do cateto oposto: '))
cat_a = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cat_o, cat_a)
print(f'A hipotenusa vai medir {hip:.2f}!')


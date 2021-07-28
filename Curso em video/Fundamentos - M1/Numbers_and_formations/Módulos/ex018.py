"""
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
ang_rad = radians(ang)
seno = sin(ang_rad)
cosseno = cos(ang_rad)
tangente = tan(ang_rad)

print(f'O ângulo {ang:.1f} é, em RADIANOS, {ang_rad:.2f}')
print(f'O ângulo {ang:.1f} é, tem SENO, {seno:.2f}')
print(f'O ângulo {ang:.1f} é, tem COSSENO, {cosseno:.2f}')
print(f'O ângulo {ang:.1f} é, tem TANGENTE, {tangente:.2f}')

"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

numero = int(input('Digite um número: '))
dobro = numero**2
triplo = numero**3
raiz = numero**0.5

print(f'''O dobro do número {numero}, é {dobro}.
Seu triplo é {triplo}.
Sua raiz é {raiz:.2f}.''')
"""
EXERCÍCIO 077: Contando Vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for cada in palavras:
    print(f'\nNa palavra {cada.upper()} temos ', end='')
    for letra in cada:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
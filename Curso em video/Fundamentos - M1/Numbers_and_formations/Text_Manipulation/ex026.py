"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
rep = frase.count('A')
first = frase.find('A') + 1
last = frase.find('A', -1) + 1 #ou frase.rfind('A')
print(f'A letra "A" aparece {rep} vezes, sua primeira posição é em {first} e a última em {last}')

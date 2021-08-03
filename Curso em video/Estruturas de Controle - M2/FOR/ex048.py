"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
print('Soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500. ')
soma = 0
for num in range(1,501,2):
    cond = num %3 ==0
    if cond:
        soma += num
    else:
        pass
print(f'A soma final desses número resulta em: {soma}')
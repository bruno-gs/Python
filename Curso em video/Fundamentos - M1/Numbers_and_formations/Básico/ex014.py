
"""
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
graus = float(input('Temperatura em Graus Celsius: '))
fahrenheit = graus * 1.8 + 32
print(f'{graus:.1f}ºC correspondem {fahrenheit:.1f}F')

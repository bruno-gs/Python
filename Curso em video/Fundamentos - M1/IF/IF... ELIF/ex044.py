"""
EXERCÍCIO 044: Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:

- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Digite o valor do produto: R$'))
print('''TIPOS DE PAGAMENTO: 
[1] DINHEIRO /CHEQUE
[2] À VISTA NO CARTÃO
[3] 2x NO CARTÃO
[4] 3x OU MAIS NO CARTÃO''')

tipo = int(input('Digite o meio de pagamento: '))

if tipo == 1:
    print(f'O valor será de: R${valor*1.1:.2f}')
elif tipo == 2:
    print(f'O valor será de: R${valor*1.05:.2f}')
elif tipo == 3: 
    print(f'O valor será de: R${valor:.2f} -- Resultando em parcelas de R${valor/2:.2f}')
else:    
    print(f'O valor será de: R${valor*1.2:.2f} -- Resultando em parcelas de R${(valor*1.2)/2:.2f}')

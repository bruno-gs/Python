"""
EXERCÍCIO 059: Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
print('Programa de Opções para dois números')
n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
maior = n1
while True:
    print('''
As opções com os dois números são: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
Para sair do programa:
    [ 5 ] Sair do Programa
    ''')
    opcao = int(input('Qual sua escolha: '))
    print()

    if opcao == 5:
        break

    elif opcao == 1:
        print(f'A soma de {n1} e {n2} resulta em {n1 + n2}')

    elif opcao == 2 : 
        print(f'A multiplicação de {n1} e {n2} resulta em {n1 * n2}')

    elif opcao == 3:
        if n2 > maior:
            maior = n2
            print(f'O maior número entre de {n1} e {n2} é o {maior}')

        elif n1 == n2:
            print(f'Os dois números são iguais, {n1}, ou seja não há um maior.')

        else:
            print(f'O maior número entre de {n1} e {n2} é o {maior}')


    elif opcao == 4:
        print('Opção para Analisar outros números')
        n1 = int(input('Digite o novo Primeiro número: '))
        n2 = int(input('Digite o novo Segundo número: '))
        maior = n1

print('FIM! Obrigado pela preferência.')    

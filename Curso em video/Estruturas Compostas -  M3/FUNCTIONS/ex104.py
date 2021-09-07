def leiaInt(msg):
    while True:
        inteiro = str(input(msg))
        if inteiro.isnumeric():
            return inteiro
            break
        else:
            print('ERRO! Digite um número válido!')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')



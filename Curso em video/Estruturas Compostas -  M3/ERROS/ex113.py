def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mErro! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031mEntrada de dados intemrrompida pelo usuário.\033[m')
            return 0
        else:
            return real


n = leiaInt('Digite um Inteiro: ')
g = leiaFloat('Digite um valor Real:')
print(f'Você digitou o número inteiro {n} e o real foi {g}.')

def voto(ano):
    from datetime import date  # com a importação dentro da função, há economia de memória
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano nasceu? '))
print(voto(nasc))

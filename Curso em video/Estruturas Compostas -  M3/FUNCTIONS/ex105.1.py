# Trata-se da resolução de modo mais fácil e utilizando outras ferramentas facilitando e diminuindo laços e verificações
def notas(*n, sit=False):
    t = dict()
    t['Total'] = len(n)
    t['Maior'] = max(n)
    t['Menor'] = min(n)
    t['Média'] = sum(n) / len(n)
    if sit:
        if t['Média'] >= 7:
            t['Situação'] = 'BOA'
        elif t['Média'] >= 5:
            t['Situação'] = 'RAZOÁVEL'
        else:
            t['Situação'] = 'RUIM'
    return t


caso = notas(2, 2, 8, 10, 5, sit=True)
print(caso)
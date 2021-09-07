def notas(* num, sit=False):
    """
    Função para verificar notas e a situação dos alunos de uma turma.
    :param num: notas dos alunos, quantas desejar!
    :param sit: situação da turma, em relação a média global
    :return: dicionário com quantas notas, maior nota, menor, média e situação.
    """
    turma = dict()
    turma['Total'] = len(num)
    mai = men = tot = 0
    for i, v in enumerate(num):
        tot += v
        if i == 0:
            mai = men = v
        else:
            if v > mai:
                mai = v
            if v < men:
                men = v
    turma['Maior'] = mai
    turma['Menor'] = men
    turma['Média'] = tot / (turma['Total'])
    if sit:
        if turma['Média'] < 5.0:
            turma['Situação'] = 'RUIM.'
        elif 5 < turma['Média'] < 7:
            turma['Situação'] = 'RAZOÁVEL.'
        elif 7 < turma['Média'] < 8.5:
            turma['Situação'] = 'BOA.'
        else:
            turma['Situação'] = 'EXCELENTE!'
    return turma


caso = notas(2, 2, 8, 10, 5, sit=True)
print(caso)

# -*- coding: utf-8 -*-

import pandas as pd

def table_five(x: list, y: list):
    """Função para geração da tabela utilizada na lista 5 (Pacote five)
    :param: x: Valores em X
    :param: y: Valores em Y
    """
    
    table = pd.Series()
    table.xy = []
    table.s_x = []
    table.s_y = []
    table.x = x
    table.y = y
    
    # Gerando tabela de xy, x ** 2, y ** 2
    for index in range(0, len(x)):
        table.xy.append(x[index] * y[index])
        table.s_x.append(x[index] ** 2)
        table.s_y.append(y[index] ** 2)
    
    # Gerando o somatório de cada um dos itens
    table.x.append(sum(table.x))
    table.y.append(sum(table.y))
    table.xy.append(sum(table.xy))
    table.s_x.append(sum(table.s_x))
    table.s_y.append(sum(table.s_y))
    
    return table
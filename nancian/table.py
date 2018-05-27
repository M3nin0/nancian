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
        table.xy.append(x[index] * y[index]) # X * Y
        table.s_x.append(x[index] ** 2) # X ^ 2
        table.s_y.append(y[index] ** 2) # Y ^ 2
    
    # Gerando o somatório de cada um dos itens
    table.x.append(sum(table.x)) # X
    table.y.append(sum(table.y)) # Y
    table.xy.append(sum(table.xy)) 
    table.s_x.append(sum(table.s_x)) 
    table.s_y.append(sum(table.s_y)) 
    
    return table

def nearest_neighbors_norm(element: float):
    """Função para buscar o elemento mais próximo de um dado elemento
    :param: element: Elemento referência na busca de proximidade
    :param: table: Tabela onde a busca será realizada
    
    Para encontrar o elemento mais próximo será utilizado a distância simples
    d = Eq - Ep
    """
    
    table = pd.read_csv('nancian/tables/normal_dist_table.csv')
    
    # Armazenamento das informações do elemento encontrado
    neighbor = {'neighbor': 0, 'column': 0, 'row': 0, 'distance': 1} 

    # Mapeia as colunas da tabela
    # Aqui a primeira está sendo desconsiderada como coluna de referência
    columns = table.columns[1:]
    
    for column in columns:
        row = 0
        for item in table[column]:
            if abs(item - element) < neighbor['distance']:
                neighbor['distance'] = abs(item - element)
                neighbor['neighbor'] = item
                neighbor['column'] = column
                neighbor['row'] = row + 2
            row += 1
    return neighbor

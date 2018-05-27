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


def nearest_neighbors(element: float, type_dist: str , typeof: str = None):
    """Função para buscar o elemento mais próximo de um dado elemento
    :param: element: Elemento referência na busca de proximidade
    :param: type_dist: Tipo de distribuição
        - normal;
        - student
    :param: typeof: Tipo de teste que está sendo realizado
        - monocaudal;
        - bicaudal.
    
    Para encontrar o elemento mais próximo será utilizado a distância simples
    d = Eq - Ep
    """
    
    if type_dist == 'normal':
        table = pd.read_csv('nancian/tables/normal_dist_table.csv')
        
        # Mapeia as colunas da tabela
        # Aqui a primeira está sendo desconsiderada como coluna de referência
        columns = table.columns[1:]
        
        # Definindo qual a diferença entre a tabela e o index
        off_set = 2
    
    elif type_dist == 'student':
        full_table = pd.read_csv('nancian/tables/student_dist_table.csv', header = None)
        table = full_table.iloc[2:]
    
        # Recriando a tabela de acordo com o tipo de teste
        if typeof == 'monocaudal':
            table.columns = list(full_table.iloc[0:1:, 0:].values[0])
        elif typeof == 'bicaudal':
            table.columns = list(full_table.iloc[1:2:, 0:].values[0])

        # Aqui a primeira está sendo desconsiderada como coluna de referência
        columns = table.columns[1:]

        # Definindo qual a diferença entre a tabela e o index
        off_set = 3

    # Armazenamento das informações do elemento encontrado
    neighbor = {'neighbor': 0, 'column': 0, 'row': 0, 'distance': 1} 
    
    for column in columns:
        row = 0
        for item in table[column]:
            if abs(item - element) < neighbor['distance']:
                neighbor['distance'] = abs(item - element)
                neighbor['neighbor'] = item
                neighbor['column'] = column
                neighbor['row'] = row + off_set
            row += 1
    return neighbor

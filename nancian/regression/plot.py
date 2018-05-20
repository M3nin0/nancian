# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot_disp(x: list, y: list, plot_title: str):
    """Função para criar diagrama de dispersão
    :param: x: Lista com os valores em X
    :param: y: Lista com os valores em Y
    :param: plot_title: Titulo do plot
    """
    
    plt.figure
    plt.title(plot_title)
    plt.plot(x, y, marker='o', linestyle='')

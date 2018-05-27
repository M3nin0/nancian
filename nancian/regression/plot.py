# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plot_disp(x: list, y: list, plot_title: str, fit_function):
    """Função para criar diagrama de dispersão
    :param: x: Lista com os valores em X
    :param: y: Lista com os valores em Y
    :param: plot_title: Titulo do plot
    :param: fit_function: Função para realização do fit da linha
    """

    # Preparando a linha de fit
    xfit, yfit = (min(x), max(x)), (fit_function(min(x)), fit_function(max(x)))
    
    plt.figure()
    plt.title(plot_title)
    plt.plot(xfit, yfit, 'b')
    plt.plot(x, y, marker='o', linestyle='')

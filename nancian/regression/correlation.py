# -*- coding: utf-8 -*-

from math import sqrt

class Pearson:
    """Classe de correlação Pearson
    """
    
    @classmethod
    def correlation(self, n, s_xy, s_x, s_y, s_x_sqrt, s_y_sqrt):
        """Método para calcular o coeficiente de correlação
        :param: n: Número de amostras
        :param: s_xy: Somatório de X * Y
        :param: s_x: Somatório de X
        :param: s_y: Somatório de Y
        :param: s_x_sqrt: Somatório de X quadrado
        :param: s_y_sqrt: Somatório de Y quadrado
        """
        
        return (n * s_xy - (s_x * s_y)) / sqrt((n * s_x_sqrt - (s_x) ** 2) * (n * s_y_sqrt - (s_y) ** 2))

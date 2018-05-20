# -*- coding: utf-8 -*-

IS_POSITIVE = {True: '+', False: ''} 

class Linear:
    """Classe da regressão linear
    """
    
    a = None
    b = None
    
    @classmethod
    def equation_line(self, n: float, s_xy: float, s_x: float, s_y: float, s_x_sqrt: float):
        """Método para encontrar a equação geral da reta utilizando o método
        de mínimos quadrados
        :param: n: Número de amostras
        :param: s_xy: Somatório de X * Y
        :param: s_x: Somatório de X
        :param: s_y: Somatório de Y
        :param: s_x_sqrt: Somatório de X quadrado
        :rtype: str
        """
        
        self.a = round((n * s_xy - (s_x * s_y)) / ((n * s_x_sqrt) - ((s_x) ** 2)), 2)
        self.b = (s_y - (self.a) * s_x) / n
        
        return 'y = {}x{}{}'.format(round(self.a, 2), IS_POSITIVE[self.b > 0] , round(self.b, 2))
    
    @classmethod
    def estimate_x(self, x: float):
        """Método para estimar o valor de acordo com a expressão da reta encontrada
        :param: x: Valor que será aplicado na equação da reta
        """
        
        try:
            return (self.a * x) + self.b
        except:
            print('Encontre primeiro a equação da reta!')

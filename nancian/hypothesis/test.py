from math import sqrt

class HypothesisTest:
    """Classe com facilidades para a solução dos testes de hipótese
    """

    @classmethod
    def calc_t(self, x: float, m: float, s: float, n: float):
        """Método para cálcular a hipótese teste T para média
        :param: x: Média amostral
        :param: m: Probabilidade da hipótese nula ocorrer
        :param: s: Desvio padrão amostral
        :param: n: Quantidade de amostras
        """

        return (x - m) / (s / sqrt(n))

    @classmethod
    def calc_z(self, x: float, m: float, sigma: float, n: float):
        """Método para cálcular a hipótese teste Z para média
        :param: x: Média amostral
        :param: m: Probabilidade da hipótese nula ocorrer
        :param: sigma: Desvio padrão da população (Pode ser utilizado em seu lugar o S)
        :param: n: Quantidade de amostras
        """

        return (x - m) / (sigma / sqrt(n))

    @classmethod
    def verify_hypothesis(self, typeof: str, test_value: float, veto_one: float = None, veto_one_side: str = None, veto_two: float = None):
        """Método para verificar afirmação de Ho
        :param: typeof: Indica qual tipo de teste
            - monocaudal;
            - bicaudal.
        :param: test_value: Valor resultante da hipótese teste
        :param: veto_one: Área de rejeição um (Lado esquerdo)
        :param: veto_one_side: Indica o lado do teste monocaudal (Utilizado somente no teste monocaudal)
            - left: Teste monocaudal esquerdo
            - right: Teste monocaudal direito
        :param: veto_two: Área de rejeição dois (Utilizada somente na bicaudal) (Lado direito)
        """

        result: dict = {True: 'Aceite Ho', False: 'Rejeite Ho'}

        if typeof == 'monocaudal':
            if veto_one_side == 'left':
                op = test_value > veto_one 
            elif veto_one_side == 'right':
                op = test_value < veto_one
        elif typeof == 'bicaudal':
            op = veto_one < test_value < veto_two

        return result[op]

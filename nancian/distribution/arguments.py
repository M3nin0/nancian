import math


class Binomial:
    q = None
    p = None
    k = None
    n = None
    PXk = None

    def __init__(self):
        """
        PXk -> P(X = k) - probabilidade de que o evento se realize “k vezes” em “n provas”
        p - probabilidade de sucesso
        """
        pass

    def __repr__(self):
        return "A propabilidade de que o evento se realize {0} vezes em {1} é de {2}\nou " \
               "{3:.2f}%".format(self.k, self.n, self.PXk, self.PXk * 100)

class Poisson:
    Px = None
    e = math.e
    lamb = None
    mi = None
    t = None
    X = None

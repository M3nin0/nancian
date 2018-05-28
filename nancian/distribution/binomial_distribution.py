import math


class BinomialDistribution:
    def __init__(self, arguments):
        self.arguments = arguments
        self.nk = self.arguments.n - self.arguments.k

    def calcula(self):
        self.arguments.PXk = self._a() / self._b() * self._c()
        return self.arguments

    def calculaMenorQue(self, inicio, fim):
        result = 0
        temp = None
        while inicio < fim:
            self.arguments.k = inicio
            result += self.calcula().PXk
            inicio += 1
        self.arguments.PXk = result
        return self.arguments

    def calculaMenorIgualQue(self, inicio, fim):
        return self.calculaMenorQue(inicio, fim + 1)

    def calculaMaiorQue(self, inicio, offset=0):
        result = 0
        fim = self.arguments.n + offset
        while inicio < fim:
            self.arguments.k = inicio
            result += self.calcula().PXk
            inicio += 1
        self.arguments.PXk = result
        return self.arguments

    def calculaMaiorIgualQue(self, inicio):
        return self.calculaMaiorQue(inicio, 1)

    def _a(self):
        return math.factorial(self.arguments.n)

    def _b(self):
        return math.factorial(self.arguments.k) * \
               math.factorial(self.nk)

    def _c(self):
        return math.pow(self.arguments.p, self.arguments.k) * \
               math.pow(self.arguments.q, self.nk)


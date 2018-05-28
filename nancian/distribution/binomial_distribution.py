import math


class BinomialDistribution:
    def __init__(self, arguments):
        self.arguments = arguments
        self.nk = self.arguments.n - self.arguments.k

    def calcula(self):
        self.arguments.PXk = self._a() / self._b() * self._c()
        return self.arguments

    def _a(self):
        return math.factorial(self.arguments.n)

    def _b(self):
        return math.factorial(self.arguments.k) * \
               math.factorial(self.nk)

    def _c(self):
        return math.pow(self.arguments.p, self.arguments.k) * \
               math.pow(self.arguments.q, self.nk)

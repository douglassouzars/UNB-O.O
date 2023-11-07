import math
from forma import Forma
from ponto import Ponto

# Classe que usa os pontos e cria um círculo, e depois usa a classe forma para calcular
class Circulo(Forma):
    def __init__(self, x1, y1, x2, y2):
        self.centro = Ponto(x1, y1)
        self.raio = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def Area(self):
        return math.pi * self.raio ** 2

    def Perimetro(self):
        return 2 * math.pi * self.raio
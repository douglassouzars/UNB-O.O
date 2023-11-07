import math
from forma import Forma

# Classe que usa os pontos e cria um retângulo, e depois usa a classe forma para calcular
class Retangulo(Forma):
    def __init__(self, x1, y1, x2, y2):
        self.largura = abs(x1 - x2)
        self.altura = abs(y1 - y2)

    def Area(self):
        return self.largura * self.altura

    def Perimetro(self):
        return 2 * (self.largura + self.altura)
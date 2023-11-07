import math
from forma import Forma
from ponto import Ponto

# Classe que usa os pontos e cria um triângulo, e depois usa a classe forma para calcular
class Triangulo(Forma):
    def __init__(self, x1, y1, x2, y2):
        self.ponto1 = Ponto(x1, y1)
        ponto2 = Ponto(x2, y2)
        self.ponto3 = Ponto((self.ponto1.x + ponto2.x) / 2, (self.ponto1.y + ponto2.y) / 2)

    def Area(self):
        base = 2 * abs(self.ponto3.x - self.ponto1.x)
        altura = math.sqrt(3) * abs(self.ponto3.x - self.ponto1.x) / 2
        return (base * altura) / 2

    def Perimetro(self):
        a = math.sqrt((self.ponto3.x - self.ponto1.x) ** 2 + (self.ponto3.y - self.ponto1.y) ** 2)
        perimetro = 3 * a
        return perimetro
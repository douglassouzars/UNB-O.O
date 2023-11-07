"""Objetos Geometricos em Python"""
from ponto import Ponto
from forma import Forma
from retangulo import Retangulo
from circulo import Circulo
from triangulo import Triangulo


if __name__ == "__main__":
    x1 = float(input("Quais as coordenadas do primeiro ponto? x1: "))
    y1 = float(input("Quais as coordenadas do primeiro ponto? y1: "))
    x2 = float(input("Quais as coordenadas do segundo ponto? x2: "))
    y2 = float(input("Quais as coordenadas do segundo ponto? y2: "))

    # Retângulo
    retangulo = Retangulo(x1, y1, x2, y2)
    area_retangulo = retangulo.Area()
    perimetro_retangulo = retangulo.Perimetro()
    print("Área do Retângulo:", area_retangulo)
    print("Perímetro do Retângulo:", perimetro_retangulo)

    # Círculo
    circulo = Circulo(x1, y1, x2, y2)
    area_circulo = circulo.Area()
    perimetro_circulo = circulo.Perimetro()
    print("Área do Círculo:", area_circulo)
    print("Perímetro do Círculo:", perimetro_circulo)

    # Triângulo
    triangulo = Triangulo(x1, y1, x2, y2)
    area_triangulo = triangulo.Area()
    perimetro_triangulo = triangulo.Perimetro()
    print("Área do Triângulo:", area_triangulo)
    print("Perímetro do Triângulo:", perimetro_triangulo)
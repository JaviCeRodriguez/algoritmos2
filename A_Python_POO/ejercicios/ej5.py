"""
Implemente la clase Punto (pares de coordenadas de tipo float x, y). Defina
constructores y métodos para asignar valores a las coordenadas de los puntos,
retornar el valor de cada coordenada, y sumar dos puntos, retornando su
resultado. Definir un método booleano de igualdad entre dos puntos.
"""
from typing import Optional

class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def asignar_valores(self, x: Optional[float] = None, y: Optional[float] = None) -> None:
        if x != None:
            self.x = x
        if y != None:
            self.y = y
    
    def retornar_valores(self) -> tuple[float, float]:
        return self.x, self.y
    
    def sumar_puntos(self, otro_punto: "Punto") -> "Punto":
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)
    
    def __eq__(self, otro_punto: "Punto") -> bool:
        return self.x == otro_punto.x and self.y == otro_punto.y

if __name__ == '__main__':
    punto1 = Punto(1, 2)
    punto2 = Punto(3, 4)
    punto3 = punto1.sumar_puntos(punto2)
    print(punto3.retornar_valores())
    print(punto1 == punto2)
    print(punto1 == Punto(1, 2))
    print(punto1 == Punto(3, 4))
    punto1.asignar_valores(3, 4)
    print(punto1 == punto2)
    print(punto1 == Punto(3, 4))
    print(punto1.retornar_valores())
    print(punto2.retornar_valores())
    print(punto3.retornar_valores())
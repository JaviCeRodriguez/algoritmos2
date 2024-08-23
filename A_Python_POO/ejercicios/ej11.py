"""
Definir la clase ExpresionAritmetica, que permita representar constantes
numéricas enteras, operaciones binarias de suma y producto, y operaciones
unarias de negación aritmética, incrementar y decrementar. Toda expresión
deberá poder evaluar el resultado de la expresión, retornando el valor entero
resultante. Definir tantas subclases como posibilidades existan de armar
expresiones aritméticas
"""

from abc import ABC, abstractmethod

class ExpresionAritmetica(ABC):
    @abstractmethod
    def evaluar(self):
        pass

class Constante(ExpresionAritmetica):
    def __init__(self, value):
        self.value = value

    def evaluar(self):
        return self.value
    
class Suma(ExpresionAritmetica):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluar(self):
        return self.left.evaluar() + self.right.evaluar()
    
class Producto(ExpresionAritmetica):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluar(self):
        return self.left.evaluar() * self.right.evaluar()
    
class Negacion(ExpresionAritmetica):
    def __init__(self, value):
        self.value = value

    def evaluar(self):
        return -self.value.evaluar()
    
class Incremento(ExpresionAritmetica):
    def __init__(self, value):
        self.value = value

    def evaluar(self):
        return self.value.evaluar() + 1
    
class Decremento(ExpresionAritmetica):
    def __init__(self, value):
        self.value = value

    def evaluar(self):
        return self.value.evaluar() - 1
    
if __name__ == "__main__":
    expresion = Suma(
        left=Producto(
            left=Constante(value=2),
            right=Constante(value=3)
        ),
        right=Constante(value=4)
    )
    print(expresion.evaluar())

    expresion = Negacion(
        value=Incremento(
            value=Decremento(
                value=Constante(value=5)
            )
        )
    )
    print(expresion.evaluar())

    expresion = Producto(
        left=Suma(
            left=Constante(value=2),
            right=Constante(value=3)
        ),
        right=Constante(value=4)
    )
    print(expresion.evaluar())
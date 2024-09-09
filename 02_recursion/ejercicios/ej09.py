"""
Calcular el producto de dos números enteros utilizando
recursión de cola.
"""

def producto(a: int, b: int) -> int:
    def producto_interno(a: int, b: int, resultado: int) -> int:
        if b == 0:
            return resultado
        else:
            return producto_interno(a, b - 1, resultado + a)
    
    return producto_interno(a, b, 0)


if __name__ == "__main__":
    print(producto(5, 3)) # 15
    print(producto(2, 10)) # 20
"""
Definir la función desde_hasta con recursión de cola que
dados dos números enteros retorne una lista de números
consecutivos donde el primer elemento de la lista
resultante sea el primer elemento dado, y el último
elemento de la lista resultante sea el segundo elemento
dado.
"""

def desde_hasta(desde: int, hasta: int, resultado=[]) -> list[int]:
    if desde > hasta:
        return []
    if desde == hasta:
        return resultado + [hasta]
    else:
        return desde_hasta(desde + 1, hasta, resultado + [desde])
    
if __name__ == "__main__":
    print(desde_hasta(1, 5)) # [1, 2, 3, 4, 5]
    print(desde_hasta(5, 1)) # [5, 4, 3, 2, 1]
    print(desde_hasta(1, 1)) # [1]
    print(desde_hasta(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
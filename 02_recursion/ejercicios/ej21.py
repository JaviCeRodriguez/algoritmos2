"""
Implementar la función recursiva producto_escalar,
que dados dos vectores de enteros, retorne un
entero que represente el producto escalar de ambos (iterativo)
"""

def producto_escalar(v1: list[int], v2: list[int]) -> int:
    if len(v1) != len(v2):
        raise ValueError('Los vectores deben tener la misma longitud')

    producto = 0
    for i in range(len(v1)):
        producto += v1[i] * v2[i]
    return producto

if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(producto_escalar(v1, v2)) # 32
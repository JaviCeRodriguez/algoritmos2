"""
Definir la función intercalar con recursión de pila, que
dados dos listas de enteros, retorne una lista de enteros
que corresponda al intercalado elemento a elemento a
elemento de las dos listas dadas.
"""

def intercalar(a: list[int], b: list[int]) -> list[int]:
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    intercalado_parcial = intercalar(a[1:], b[1:])
    return [a[0], b[0]] + intercalado_parcial

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]
print(intercalar(lista_a, lista_b)) # [1, 5, 2, 6, 3, 7, 4, 8]
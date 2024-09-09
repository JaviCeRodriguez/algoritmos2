"""
Definir la función cantidad, que dada una lista
de enteros y un número n, retorne la cantidad de
apariciones del número n en la lista dada.

Usar recursión de pila (esto lo agrego yo, no está en el enunciado original)
"""

def cantidad(lista: list[int], n: int) -> int:
    if lista == []:
        return 0
    else:
        if lista[0] == n:
            return 1 + cantidad(lista[1:], n)
        else:
            return cantidad(lista[1:], n)


if __name__ == "__main__":
    print(cantidad([1, 2, 3, 4, 5], 1)) # 1
    print(cantidad([1, 2, 3, 4, 5], 6)) # 0
    print(cantidad([1, 2, 3, 4, 5, 1, 1], 1)) # 3
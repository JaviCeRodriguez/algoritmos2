"""
Implementar la función recursiva busqueda_binaria, que
dado un vector ordenado de enteros y un entero dado,
retorne si el entero dado pertenece a alguna posición del
vector. La búsqueda deberá efectuarse con la técnica de
búsqueda binaria. Usar recursión de cola
"""

def busqueda_binaria(vector: list[int], n: int) -> bool:
    def _busqueda_binaria(vector: list[int], n: int, inicio: int, fin: int) -> bool:
        if inicio > fin:
            return False
        medio = (inicio + fin) // 2
        if vector[medio] == n:
            return True
        elif vector[medio] > n:
            return _busqueda_binaria(vector, n, inicio, medio - 1)
        else:
            return _busqueda_binaria(vector, n, medio + 1, fin)
    return _busqueda_binaria(vector, n, 0, len(vector) - 1)

if __name__ == '__main__':
    vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(busqueda_binaria(vector, 5)) # True
    print(busqueda_binaria(vector, 11)) # False
    print(busqueda_binaria(vector, 0)) # False
    print(busqueda_binaria(vector, 1)) # True
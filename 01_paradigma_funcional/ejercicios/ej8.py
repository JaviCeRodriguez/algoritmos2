"""
Definir utilizando reduce una operación que dada una lista de cadenas devuelva
un diccionario donde las claves sean cada elemento de la lista y los valores sean
la cantidad de apariciones que tiene ese elemento en la lista.
Ejemplo: contar(['a', 'b', 'c', 'a', 'a', 'c', 'b', 'd', 'c', 'a', 'e']) -> {'a': 4, 'b': 2, 'c': 3, 'd': 1,
'e': 1}.
"""

from typing import List
from functools import reduce

def contar(lista: List[str]) -> dict[str, int]:
    return reduce(lambda acc, elemento: {**acc, elemento: acc.get(elemento, 0) + 1}, lista, {})

# El ** en el diccionario es para desempaquetar el diccionario acc y agregarle el nuevo elemento con su valor

if __name__ == "__main__":
    lista = ["a", "b", "c", "a", "a", "c", "b", "d", "c", "a", "e"]
    print(contar(lista))  # {'a': 4, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
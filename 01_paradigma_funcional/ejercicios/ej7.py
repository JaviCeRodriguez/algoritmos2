"""
A través del uso del map, dada una lista de cadenas generar una nueva lista
que devuelva la cantidad que tiene de cierta letra (pasada como argumento)
cada elemento.
Por ejemplo, si queremos contar la letra 'a' en ['casa', 'hogar', 'espacio',
'cuento'] deberíamos obtener [2, 1, 1, 0].
"""

from typing import List

def contar_letra(lista: List[str], letra: str) -> List[int]:
    return list(map(lambda palabra: palabra.count(letra), lista))

if __name__ == "__main__":
    lista = ["casa", "hogar", "espacio", "cuento"]
    letra = "a"
    print(contar_letra(lista, letra))  # [2, 1, 1, 0]
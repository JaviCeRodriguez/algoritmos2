"""
Definir la función es_palindromo, que dada una lista de
entero, retorne si es o no es palíndromo, utilizando
recursividad en cola.
"""
from typing import Union

def es_palindromo(lista: list[Union[str, int]]) -> bool:
    def es_palindromo_interna(lista: list[Union[str, int]], lista_inversa: list[Union[str, int]]) -> bool:
        if len(lista) == len(lista_inversa):
            return lista == lista_inversa
        else:
            return es_palindromo_interna(
                lista=lista[1:],
                lista_inversa=lista_inversa + [lista[0]]
            )
    
    if not lista:
        return False

    if len(lista) % 2 != 0:
        lista.pop(len(lista) // 2)

    return es_palindromo_interna(lista=lista, lista_inversa=[])


if __name__ == '__main__':
    lista_1: list[Union[str, int]] = ["n", "e", "u", "q", "u", "e", "n"]
    print(es_palindromo(lista_1)) # True

    lista_2: list[Union[str, int]] = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(es_palindromo(lista_2)) # True

    lista_3: list[Union[str, int]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(es_palindromo(lista_3)) # False

    lista_4: list[Union[str, int]] = [1, 2, 3, 3, 2, 1]
    print(es_palindromo(lista_4)) # True
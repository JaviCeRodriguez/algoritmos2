"""
Definir la función aplanar, que dada una lista de listas de enteros,
retorne una lista de enteros que corresponda a la concatenación de
elementos-lista de la lista original.

Por ejemplo: aplanar([[5,7], [], [3,7,2], [9]]) = [5, 7, 3, 7, 2, 9]
Puede tener 1 o más listas anidadas.
"""

def aplanar_cola(lista: list) -> list:
    def aplanar_interna(lista: list, resultado: list) -> list:
        if not lista:
            return resultado
        else:
            # Chequeo si el primer elemento de la lista es una lista
            if isinstance(lista[0], list):
                return aplanar_interna(
                    lista=lista[1:],
                    resultado=aplanar_interna(lista=lista[0], resultado=resultado)
                )
            # Si no es una lista, concateno el elemento a la lista resultado
            else:
                return aplanar_interna(
                    lista=lista[1:],
                    resultado=resultado + [lista[0]]
                )
    
    return aplanar_interna(lista=lista, resultado=[])


def aplanar_pila(lista):
    if not lista:
        return []
    else:
        if isinstance(lista[0], list):
            return aplanar_pila(lista[0]) + aplanar_pila(lista[1:])
        else:
            return [lista[0]] + aplanar_pila(lista[1:])

if __name__ == '__main__':
    lista = [[5, 7], [], [3, 7, 2], [9]]
    print(aplanar_cola(lista)) # [5, 7, 3, 7, 2, 9]
    print(aplanar_pila(lista)) # [5, 7, 3, 7, 2, 9]

    lista = [[1, 2, 3, [4, 5, 6]], [7, 8, 9]]
    print(aplanar_cola(lista)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(aplanar_pila(lista)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
Definir la función sublista, que dada una lista de enteros, un
número que represente una posición y otro número que
represente una longitud, devuelva una lista de enteros (que
se basa en la lista dada) que comience en la posición dada y
que tenga la longitud dada desde esa posición (pila)

16bis: sublista_cola

16bis bis: sublista_iterativa
"""

def sublista(lista: list[int], posicion: int, longitud: int) -> list[int]:
    if posicion == 0:
        if longitud == 0:
            return []
        else:
            return [lista[0]] + sublista(lista[1:], posicion, longitud - 1)
    else:
        return sublista(lista[1:], posicion - 1, longitud)


def sublista_cola(lista: list[int], posicion: int, longitud: int) -> list[int]:
    def sublista_interna(lista: list[int], posicion: int, longitud: int, resultado=[]) -> list[int]:
        if posicion == 0:
            if longitud == 0:
                return resultado
            else:
                return sublista_interna(lista[1:], posicion, longitud - 1, resultado + [lista[0]])
        else:
            return sublista_interna(lista[1:], posicion - 1, longitud, resultado)
    
    return sublista_interna(lista, posicion, longitud)


def sublista_iterativa(lista: list[int], posicion: int, longitud: int) -> list[int]:
    nueva_lista = []
    for i in range(posicion, posicion + longitud):
        nueva_lista.append(lista[i])
    return nueva_lista
    

if __name__ == "__main__":
    print(sublista([1, 2, 3, 4, 5], 2, 3)) # [3, 4, 5]
    print(sublista([1, 2, 3, 4, 5], 0, 3)) # [1, 2, 3]
    print(sublista([1, 2, 3, 4, 5], 1, 3)) # [2, 3, 4]
    print(sublista([1, 2, 3, 4, 5], 4, 1)) # [5]
    print(sublista([1, 2, 3, 4, 5], 2, 0)) # []

    print(sublista_cola([1, 2, 3, 4, 5], 2, 3)) # [3, 4, 5]

    print(sublista_iterativa([1, 2, 3, 4, 5], 2, 3)) # [3, 4, 5]
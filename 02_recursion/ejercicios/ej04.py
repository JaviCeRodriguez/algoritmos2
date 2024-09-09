"""
Eliminar la recursión del siguiente código
"""

def longitud_recursiva(lista: list[int], contador=0) -> int:
    if not lista:
        return contador
    else:
        return longitud_recursiva(lista[1:], contador + 1)
    
def longitud_iterativa(lista: list[int], contador=0) -> int:
    while lista:
        contador += 1
        lista = lista[1:]
    return contador


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(longitud_recursiva(lista)) # 5
    print(longitud_iterativa(lista)) # 5

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(longitud_recursiva(lista)) # 10
    print(longitud_iterativa(lista)) # 10

    lista = [1]
    print(longitud_recursiva(lista)) # 1
    print(longitud_iterativa(lista)) # 1
    
    lista = []
    print(longitud_recursiva(lista)) # 0
    print(longitud_iterativa(lista)) # 0
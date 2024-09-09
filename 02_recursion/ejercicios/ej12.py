"""
Implementa una función recursiva de cola
para encontrar el máximo elemento en una
lista de enteros
"""

def maximo(lista: list[int]) -> int:
    def maximo_interna(lista: list[int], maximo: int) -> int:
        if not lista:
            return maximo
        else:
            return maximo_interna(
                lista=lista[1:],
                maximo=max(maximo, lista[0])
            )
    
    return maximo_interna(lista=lista, maximo=lista[0])


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(maximo(lista)) # 5
    lista_neg_pos = [-1, -2, -3, 4, 5]
    print(maximo(lista_neg_pos)) # 5
    lista_neg = [-1, -2, -3, -4, -5]
    print(maximo(lista_neg)) # -1
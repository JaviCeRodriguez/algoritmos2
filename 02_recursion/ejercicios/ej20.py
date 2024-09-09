"""
Implementar la función recursiva
posiciones_pares, que dado una lista de enteros,
imprima el contenido de sus posiciones pares
"""

# Recursividad de cola
# def posiciones_pares(lista: list[int]) -> None:
#     def posiciones_pares_interna(lista: list[int], indice: int) -> None:
#         if not lista:
#             return
#         else:
#             if indice % 2 == 0:
#                 print(lista[0])
#             posiciones_pares_interna(lista=lista[1:], indice=indice + 1)
    
#     posiciones_pares_interna(lista=lista, indice=0)


# Recursividad de pila
def posiciones_pares(lista: list[int]) -> None:
    if not lista:
        return
    else:
        print(lista[0])
        posiciones_pares(lista[2:])


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posiciones_pares(lista) # 1, 3, 5, 7, 9
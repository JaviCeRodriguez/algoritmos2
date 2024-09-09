"""
Identificar la recursividad de pila y de
cola en las siguientes operaciones:
"""

def producto(xs: list[int]) -> int:
    def producto_recursivo(xs: list[int], indice: int, acumulador: int) -> int:
        if indice == len(xs):
            return acumulador  
        else:
            return producto_recursivo(xs, indice + 1, acumulador * xs[indice])

    return producto_recursivo(xs, 0, 1)


def pares(xs: list[int], pares_encontrados=[]) -> list[int]:
    if xs == []:
        return pares_encontrados
    else:
        if xs[0] % 2 == 0:
            pares_encontrados.append(xs[0])
    return pares(xs[1:], pares_encontrados)

# Ambas son de cola, ya que no hay operaciones que se realicen después de la llamada recursiva
# en la función producto y pares, se realiza la llamada recursiva y se retorna el resultado de la misma.

if __name__ == "__main__":
    print(producto([1, 2, 3, 4, 5]))
    print(pares([1, 2, 3, 4, 5]))
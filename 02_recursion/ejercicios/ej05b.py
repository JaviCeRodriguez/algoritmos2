"""
Implementar una versión con recursión de cola que produzca
el resultado esperado al pasar una lista:
suma_resta_alternada([1, 2, 3, 4, 5]) = 1 + 2 - 3 + 4 - 5

Crear luego una versión iterativa de la función.
"""

def suma_resta_alternada(lista: list[int]) -> int:
    def operacion_interna(lista: list[int], suma: int, signo: int) -> int:
        if not lista:
            return suma
        else:
            return operacion_interna(lista[1:], suma + signo * lista[0], -signo)
    
    return operacion_interna(lista, 0, 1)


def suma_resta_alternada_iterativa(lista: list[int]) -> int:
    suma = 0
    signo = 1
    for num in lista:
        suma += signo * num
        signo = -signo
    return suma


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(suma_resta_alternada(lista)) # 3
    print(suma_resta_alternada_iterativa(lista)) # 3
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(suma_resta_alternada(lista)) # -5
    print(suma_resta_alternada_iterativa(lista)) # -5
    lista = [1]
    print(suma_resta_alternada(lista)) # 1
    print(suma_resta_alternada_iterativa(lista)) # 1
    lista = []
    print(suma_resta_alternada(lista)) # 0
    print(suma_resta_alternada_iterativa(lista)) # 0
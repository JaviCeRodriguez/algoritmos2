"""
Implementar una versión con recursión de cola que produzca
el resultado esperado al pasar una lista:
suma_resta_alternada([1, 2, 3, 4, 5]) = 1 + 2 - 3 + 4 - 5
"""

def suma_resta_alternada(lista: list[int]) -> int:
    def operacion_interna(lista: list[int], suma: int, signo: int, paso: int) -> int:
        print(f'lista: {lista}, suma: {suma}, signo: {signo}')
        if paso == 1:
            signo = -signo
        if not lista:
            return suma
        else:
            return operacion_interna(lista[1:], suma + signo * lista[0], -signo, paso + 1)
    
    return operacion_interna(lista, 0, 1, 0)


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(suma_resta_alternada(lista)) # 3
    # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(suma_resta_alternada(lista)) # -5
    # lista = [1]
    # print(suma_resta_alternada(lista)) # 1
    # lista = []
    # print(suma_resta_alternada(lista)) # 0
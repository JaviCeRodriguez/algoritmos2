"""
Escribir una función recursiva de cola que tome un número entero
positivo como entrada y devuela la suma de sus dígitos. Por ejemplo,
la suma de los dígitos de 123 sería 1 + 2 + 3 = 6.
"""

def suma_digitos(numero: int) -> int:
    def suma_digitos_interna(numero: int, suma: int) -> int:
        if numero == 0:
            return suma
        else:
            return suma_digitos_interna(numero // 10, suma + numero % 10)
    
    return suma_digitos_interna(numero, 0)


if __name__ == '__main__':
    numero = 123
    print(suma_digitos(numero)) # 6
    numero = 123456789
    print(suma_digitos(numero)) # 45
    numero = 0
    print(suma_digitos(numero)) # 0
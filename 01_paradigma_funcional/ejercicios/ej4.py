"""
Implementar una función generadora que permita producir todos los números
primos uno a uno.
Nota: Un número es primo si no es divisible por ningún número entre 2 y su raíz
cuadrada.
"""

from typing import Generator

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

def generador_primos() -> Generator[int, None, None]:
    numero = 2
    while True:
        if es_primo(numero):
            yield numero
        numero += 1

if __name__ == "__main__":
    generador = generador_primos()
    for _ in range(10):
        print(next(generador))
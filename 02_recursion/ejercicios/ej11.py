"""
Calcular la potencia de dos números
positivos utilizando recursión de cola
"""

def potencia(base: int, exponente: int) -> int:
    def potencia_interna(base: int, exponente: int, resultado: int) -> int:
        if exponente == 0:
            return resultado
        else:
            return potencia_interna(
                base=base,
                exponente=exponente - 1,
                resultado=resultado * base
            )
    
    return potencia_interna(base=base, exponente=exponente, resultado=1)


if __name__ == '__main__':
    resultado = potencia(2, 3)
    print(resultado) # 8
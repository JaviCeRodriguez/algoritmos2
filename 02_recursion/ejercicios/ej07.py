"""
Implementa una función que invierta una
cadena utilizando recursión de cola
"""

def invertir_cadena(cadena: str) -> str:
    def invertir_cadena_interna(cadena: str, indice: int, resultado: str) -> str:
        if indice == -1:
            return resultado
        else:
            return invertir_cadena_interna(cadena, indice - 1, resultado + cadena[indice])
    
    return invertir_cadena_interna(cadena, len(cadena) - 1, '')


def invertir_cadena_iterativa(cadena: str) -> str:
    resultado = ''
    for i in range(len(cadena) - 1, -1, -1):
        resultado += cadena[i]
    return resultado


if __name__ == "__main__":
    cadena = "hola"
    print(invertir_cadena(cadena)) # aloh
    print(invertir_cadena_iterativa(cadena)) # aloh

    cadena = "neuquen"
    print(invertir_cadena(cadena)) # neuquen
    print(invertir_cadena_iterativa(cadena)) # neuquen

    cadena = "anita lava la tina"
    print(invertir_cadena(cadena)) # anit al aval atin
    print(invertir_cadena_iterativa(cadena)) # anit al aval atin
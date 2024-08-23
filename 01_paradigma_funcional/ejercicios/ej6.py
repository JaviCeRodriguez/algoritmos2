"""
Se pide implementar una función decoradora acepta_no_valor que permita
adaptar una función con un único parámetro de cualquier tipo no nulo de forma
que devuelva la evaluación de esa función si el argumento recibido no es None.
De lo contrario, debe devolver None.
TIP: Se puede usar el hint de tipo de retorno de la decoradora como: Callable[[T |
None], R | None]. Ver Generics.
"""

from typing import Callable, TypeVar, Union

T = TypeVar("T")
R = TypeVar("R")

# Explicación: T y R son variables de tipo que se utilizan para definir el tipo de
# los parámetros y el tipo de retorno de la función decoradora.

def acepta_no_valor(funcion: Callable[[T], R]) -> Callable[[Union[T, None]], Union[R, None]]:
    def decorador(parametro: Union[T, None]) -> Union[R, None]:
        if parametro is not None:
            return funcion(parametro)
        
        return None
    
    return decorador

@acepta_no_valor
def cuadrado(numero: int) -> int:
    return numero ** 2

if __name__ == "__main__":
    print(cuadrado(5))
    print(cuadrado(None))
    print(cuadrado(0))
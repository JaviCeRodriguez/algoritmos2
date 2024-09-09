"""
Implementar la recursión de cola de Fibonacci
"""

def fibonacci(n: int) -> int:
    def fibonacci_interna(n: int, a: int, b: int) -> int:
        if n == 0:
            return a
        else:
            return fibonacci_interna(n - 1, b, a + b)
    
    return fibonacci_interna(n, 0, 1)

"""
¿Se puede? ¿Por qué?

La recursión de cola se puede implementar en la función fibonacci_interna, ya que
no hay operaciones que se realicen después de la llamada recursiva.
"""

if __name__ == "__main__":
    print(fibonacci(0)) # 0
    print(fibonacci(6)) # 8
    print(fibonacci(14)) # 377
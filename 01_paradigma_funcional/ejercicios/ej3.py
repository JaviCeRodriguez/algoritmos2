"""
Proponer ejemplos de funciones impuras para cada tipo de efecto secundario
mencionado y cómo se podrían convertir, si es posible, a versiones de funciones
pura
"""
import requests
import random

# Efecto secundario 1: Modificación de variables globales
# Función impura
def impura_1() -> None:
    global variable_global
    variable_global = 1

variable_global = 0

# Función pura
def pura_1(variable_global: int) -> int:
    return variable_global + 1

# Efecto secundario 2: Modificación de Argumentos
# Función impura
def impura_2(argumento: int) -> None:
    argumento += 1

# Función pura
def pura_2(argumento: int) -> int:
    return argumento + 1

# Efecto secundario 3: Operaciones de Entrada/Salida (I/O)
# Función impura
def impura_3() -> None:
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola, mundo!")

# Función pura
def pura_3() -> str:
    return "Hola, mundo!"

# Efecto secundario 4: Impresiones en Consola o Registro de Eventos
# Función impura
def impura_4() -> None:
    print("Hola, mundo!")

# Función pura
def pura_4() -> str:
    return "Hola, mundo!"

# Efecto secundario 5: Interacciones de Red
# Función impura
def impura_5() -> None:
    response = requests.get("https://www.google.com")
    print(response.status_code)

# Función pura
def pura_5(response: requests.Response) -> int:
    return response.status_code

# Efecto secundario 6: Llamadas a Funciones con Efectos Secundarios
# Función impura
def impura_6() -> None:
    impura_1()

# Función pura
def pura_6(argumento) -> int:
    return "cualquier cosa que sirva para la función pura_1"

# Efecto secundario 7: Generación de Números Aleatorios (????)
# Función impura
def impura_7() -> int:
    return random.randint(1, 10)

# Función pura
def pura_7(seed) -> int:
    random.seed(seed)
    return random.randint(1, 10)
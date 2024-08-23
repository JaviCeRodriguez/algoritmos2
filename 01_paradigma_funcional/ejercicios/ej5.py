"""
A lo largo de nuestro programa es posible que necesitemos almacenar
información de interés en el log de ejecución. A efectos prácticos, nuestro destino
de log será la consola, por lo que podemos utilizar simplemente un print() para
registrar un mensaje de log.
Implementar una función log currificada que permita registrar un mensaje de log y
el tipo, que puede ser error, alerta o información. 
"""

from typing import Callable

def log(tipo: str) -> Callable[[str], None]:
    def log_mensaje(mensaje: str) -> None:
        print(f"[{tipo.upper()}] {mensaje}")
    
    return log_mensaje

if __name__ == "__main__":
    log_error = log("error")
    log_alerta = log("alerta")
    log_informacion = log("información")

    log_error("Esto es un error")
    log_alerta("Esto es una alerta")
    log_informacion("Esto es una información")
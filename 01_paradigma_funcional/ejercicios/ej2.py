"""
Implementar una versión de un conjunto de elementos de cualquier tipo que
sea inmutable. Podemos apoyarnos en la tuple de Python. El conjunto se
crea con una cantidad de elementos variables y luego ya no puede
modificarse.
"""

# Clases inmutables usando dataclass

from dataclasses import dataclass
from typing import Any, Tuple

@dataclass(frozen=True)
class MateAmargo:
    ingredientes: Tuple[Any, ...]

    def __str__(self) -> str:
        mensaje = "Mate amargo con los siguientes ingredientes:"
        for ingrediente in self.ingredientes:
            mensaje += f"\n\t- {ingrediente}"
        
        return mensaje
    

mate = MateAmargo(("yerba", "agua"))
print(mate)
mate.ingredientes = ("yerba", "agua", "azúcar")  # AttributeError: can't set attribute
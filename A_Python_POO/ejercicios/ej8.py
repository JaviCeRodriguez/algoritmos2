"""
Una empresa ferroviaria administra viajes en tren entre dos estaciones terminales de su red.
Un viaje tiene asociado un trayecto (desde una estación terminal de origen a una de destino, con una distancia
determinada y una cantidad de estaciones), una cierta cantidad de vagones y una capacidad máxima de
pasajeros.

También posee qué tipo de viaje corresponde en relación a sus características técnicas, si es un viaje con
tecnología diesel, si es eléctrico o si es de alta velocidad (esto es independiente del trayecto recorrido).
    ● Viaje diesel: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
    cantidad de estaciones dividido 2 sumada a la cantidad de estaciones y de pasajeros dividido 10.
    ● Viaje eléctrico: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
    cantidad de estaciones dividido 2.
    ● Viaje de alta velocidad: El tiempo de demora promedio -en minutos- es la distancia en kilómetros dividido 10.

Definir dentro de la clase Viaje el método tiempoDeDemora, que retorne la cantidad de minutos que tarda en
efectuar su recorrido con las siguientes variantes:
    a) Especializando la clase Viaje en función del tipo de viaje.
    b) Sin especializar la clase Viaje, relacionándola con la clase TipoDeViaje, que está especializada por cada tipo
    de viaje.
"""
from typing import Literal 

Tipo = Literal["diesel", "electrico", "alta_velocidad"]

class Viaje:
    def __init__(self, origen: str, destino: str, distancia: float, estaciones: int, vagones: int, capacidad: int) -> None:
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.estaciones = estaciones
        self.vagones = vagones
        self.capacidad = capacidad
    
    def tiempo_de_demora(self) -> float:
        return self.distancia / 10

class TipoDeViaje:
    def __init__(self, tipo: Tipo) -> None:
        self.tipo = tipo
    
    def tiempo_de_demora(self, viaje: Viaje) -> float:
        if self.tipo == "diesel":
            return viaje.distancia * viaje.estaciones / 2 + viaje.estaciones + viaje.capacidad / 10
        elif self.tipo == "electrico":
            return viaje.distancia * viaje.estaciones / 2
        else: # self.tipo == "alta_velocidad"
            return viaje.distancia / 10

if __name__ == "__main__":
    viaje = Viaje(
        origen="Buenos Aires",
        destino="Mar del Plata",
        distancia=400,
        estaciones=10,
        vagones=5,
        capacidad=200
    )
    tipo_diesel = TipoDeViaje(tipo="diesel")
    tipo_electrico = TipoDeViaje(tipo="electrico")
    tipo_alta_velocidad = TipoDeViaje(tipo="alta_velocidad")
    
    print(tipo_diesel.tiempo_de_demora(viaje=viaje))
    print(tipo_electrico.tiempo_de_demora(viaje=viaje))
    print(tipo_alta_velocidad.tiempo_de_demora(viaje=viaje))
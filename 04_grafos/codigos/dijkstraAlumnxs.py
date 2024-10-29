from typing import Generic, TypeVar
T = TypeVar('T')

class GrafoConjuntos(Generic[T]):
    def __init__(self):
        self.nodos: set[T] = set()
        self.aristas: dict[tuple[T, T], int] = {}

    def agregar_nodo(self, nodo: T):
        self.nodos.add(nodo)

    def agregar_arista(self, origen: T, destino: T, peso: int):
        if origen in self.nodos and destino in self.nodos:
            if isinstance(peso, int) and peso > 0:
                self.aristas[(origen, destino)] = peso
            else:
                raise ValueError("El peso de la arista debe ser un entero positivo")

    def eliminar_nodo(self, nodo: T):
        self.nodos.discard(nodo)
        aristas_sin_nodo = {
            (origen, destino): peso
            for (origen, destino), peso in self.aristas.items()
            if origen != nodo and destino != nodo
        }
        self.aristas = aristas_sin_nodo

    def eliminar_arista(self, origen: T, destino: T):
        self.aristas.pop((origen, destino), None)

    def es_vecino_de(self, origen: T, destino: T) -> bool:
        return (origen, destino) in self.aristas or (destino, origen) in self.aristas

    def vecinos_de(self, nodo: T) -> set[T]:
        vecinos = set()
        for (origen, destino), peso in self.aristas.items():
            if origen == nodo:
                vecinos.add(destino)
            elif destino == nodo:
                vecinos.add(origen)
        return vecinos

    def peso_arista(self, origen: T, destino: T) -> int:
        return self.aristas.get((origen, destino), self.aristas.get((destino, origen), None))


grafo = GrafoConjuntos[str]()
grafo.agregar_nodo("a")
grafo.agregar_nodo("b")
grafo.agregar_nodo("c")
grafo.agregar_nodo("d")
grafo.agregar_nodo("e")
grafo.agregar_nodo("f")
grafo.agregar_arista("a", "b", 5)
grafo.agregar_arista("a", "c", 2)
grafo.agregar_arista("a", "d", 3)
grafo.agregar_arista("b", "c", 1)
grafo.agregar_arista("b", "e", 1)
grafo.agregar_arista("b", "f", 3)
grafo.agregar_arista("d", "e", 2)
grafo.agregar_arista("e","f", 1)
#print(grafo.dijkstra("a","f"))
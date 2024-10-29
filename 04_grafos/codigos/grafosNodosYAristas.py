from typing import Generic, TypeVar
T = TypeVar('T')


class Grafo(Generic[T]):
    # Constructor de la clase, inicializa el grafo con conjuntos vacíos de vértices y aristas
    def __init__(self, vertices: set[T] = set(), aristas: set[tuple[T, T]] = set()) -> None:
        self.vertices = vertices  # Conjunto de vértices o nodos del grafo
        self.aristas = aristas    # Conjunto de aristas, que son pares de vértices

    # Método para agregar un nodo (vértice) al grafo
    def agregar_nodo(self, nodo: T) -> None:
        # Si el nodo no está en el conjunto de vértices, lo agrega
        if nodo not in self.vertices:
            self.vertices.add(nodo)
        # Si el nodo ya existe, lanza un error
        else:
            raise ValueError(f"El nodo {nodo} ya pertenece al grafo.")

    # Método para agregar una arista al grafo (una conexión entre dos nodos)
    def agregar_arista(self, arista: tuple[T, T]) -> None:
        # Si la arista o su versión invertida ya están en el grafo, lanza un error
        if arista in self.aristas or arista[::-1] in self.aristas:
            raise ValueError(f"La arista {arista} ya pertenece al grafo.")
        # Si no existe, agrega la arista al conjunto
        else:
            self.aristas.add(arista)

    # Método para eliminar un nodo del grafo
    def eliminar_nodo(self, nodo: T) -> None:
        # Si el nodo no está en el conjunto de vértices, lanza un error
        if nodo not in self.vertices:
            raise ValueError(f"El nodo {nodo} no pertenece al grafo.")
        else:
            self.vertices.remove(nodo)  # Elimina el nodo del conjunto de vértices
            # Elimina todas las aristas asociadas con ese nodo
            self.aristas = {arista for arista in self.aristas if nodo not in arista}

    # Método para eliminar una arista del grafo
    def eliminar_arista(self, arista: tuple[T, T]) -> None:
        # Si la arista no está en el conjunto (ni su versión invertida), lanza un error
        if arista not in self.aristas and arista[::-1] not in self.aristas:
            raise ValueError(f"La arista {arista} no pertenece al grafo.")
        else:
            # Elimina la arista tanto en su forma original como en su versión invertida
            self.aristas.discard(arista)
            self.aristas.discard(arista[::-1])  # forma de invertir la tupla arista. El operador [::-1] es una slicing operation

    # Método para verificar si dos nodos son vecinos (están conectados por una arista)
    def es_vecino_de(self, nodoA: T, nodoB: T) -> bool:
        # Devuelve True si existe una arista entre los nodos, ya sea en el orden dado o invertido
        return (nodoA, nodoB) in self.aristas or (nodoB, nodoA) in self.aristas

    # Método para obtener una lista de vecinos (nodos conectados) de un nodo dado
    def vecinos_de(self, nodo: T) -> list[T]:
        vecinos = []  # Inicializa una lista vacía para almacenar los vecinos
        # Recorre todas las aristas del grafo
        for arista in self.aristas:
            # Si el nodo dado es uno de los nodos de la arista
            if nodo in arista:
                # Si el nodo es el primer elemento de la arista, el vecino es el segundo y viceversa
                vecino = arista[0] if arista[1] == nodo else arista[1]
                vecinos.append(vecino)  # Añade el vecino a la lista
        return vecinos  # Devuelve la lista de vecinos
    
    def __str__(self) -> str:
        return f"Vertices = {self.vertices} \n Aristas = {self.aristas}"

grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)

# Agregar aristas
grafo.agregar_arista((1, 2))
grafo.agregar_arista((2, 3))
grafo.agregar_arista((3, 4))
grafo.agregar_arista((4, 1))

# Mostrar 
print("Grafo hasta ahora",grafo)

# Eliminar nodo y arista
grafo.eliminar_nodo(2)
grafo.eliminar_arista((3, 4))

# Verificar vecinos
print("\n¿El nodo 1 es vecino del nodo 3?", grafo.es_vecino_de(1, 3))
print("\n¿El nodo 3 es vecino del nodo 4?", grafo.es_vecino_de(1, 4))
print("Vecinos del nodo 1:", grafo.vecinos_de(1))
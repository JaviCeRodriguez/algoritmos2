from grafosNodosYAristas import Grafo as GrafoBase, T

class Grafo(GrafoBase[T]):
    def dfs(self) -> list[T]:
        """
        DFS Principal:
            1) Inicializar recorrido vacío
            2) Buscar un nodo sin visitar
            3) Recorrer DFS comenzando en el nodo obtenido
            en 2) → en este caso se puede hacer por grafo no dirigido y todos los nodos conectados
            4) Mientras existan nodos sin visitar, volver a 2) (cuando el grafo no es conexo y
            queremos recorrer todo el grafo)
        
        DFS2:
            1) Si el nodo actual no fue visitado (sirve para evitar entrar en bucles):
            a) Agregarlo al recorrido
            b) Para cada vecino del nodo actual recorrerlo en profundidad (recursión)
        """
        recorrido = []
        visitados = set()

        for nodo in self.vertices:
            if nodo not in visitados:
                self._dfs(nodo, visitados, recorrido)
        return recorrido
    
    def _dfs(self, nodo: T, visitados: set[T], recorrido: list[T]) -> None:
        if nodo not in visitados:
            recorrido.append(nodo)
            visitados.add(nodo)
            for vecino in self.vecinos_de(nodo):
                self._dfs(vecino, visitados, recorrido)

    def bfs(self) -> list[T]:
        """
        BFS Principal (inicializa el recorrido)
            1) Inicializar recorrido vacío
            2) Buscar un nodo sin visitar (hasta acá idem dfs)
            3) Recorrer BFS comenzando con el nodo obtenido
            en 2), encolándolo en una cola. Diferencia:no lo vamos a recorrer como parámetro
            como un nodo más, que se pasa a bfs2.
            4) Mientras haya nodos sin visitar, recorrerlos con BFS como
            en el paso 3) (hace los pasos 2) y 3)) para, partes no conexas del grafo, o si fuera dirigido)
        
        BFS2 (realiza el recorrido a lo ancho)
            1) Si hay nodos encolados, continuar con el paso 2)
            2) Desencolar un nodo de la cola
            3) Si el nodo desencolado no fue visitado
            a) Agregarlo al recorrido
            b) Para cada vecino del nodo actual, encolarlo
            4) Invocar BFS nuevamente con la cola modificada (recursión)
        """
        recorrido = []
        visitados = set()
        for nodo in self.vertices:
            if nodo not in visitados:
                self._bfs(nodo, visitados, recorrido)
        return recorrido
    
    def _bfs(self, nodo: T, visitados: set[T], recorrido: list[T]) -> None:
        cola = [nodo]
        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual not in visitados:
                recorrido.append(nodo_actual)
                visitados.add(nodo_actual)
                for vecino in self.vecinos_de(nodo_actual):
                    cola.append(vecino)


if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_nodo(1)
    grafo.agregar_nodo(2)
    grafo.agregar_nodo(3)
    grafo.agregar_nodo(4)
    grafo.agregar_nodo(5)
    grafo.agregar_nodo(6)
    grafo.agregar_nodo(7)

    grafo.agregar_arista((1, 2))
    grafo.agregar_arista((1, 3))
    grafo.agregar_arista((2, 4))
    grafo.agregar_arista((4, 7))
    grafo.agregar_arista((2, 5))
    grafo.agregar_arista((3, 6))
    grafo.agregar_arista((5, 6))

    print(grafo.dfs())  # [1, 2, 4, 7, 5, 6, 3]

    print(grafo.bfs())  # [1, 2, 3, 4, 5, 6, 7]
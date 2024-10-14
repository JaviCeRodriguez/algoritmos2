"""
Ejercicios

01: Desarrollar las funciones de postorder con las mismas tres estrategias vistas, que
devuelva una lista con el orden de los nodos visitados.

02: Implementar la función nivel, que dado un valor contenido en el árbol, devuelva
el nivel del mismo. Debe contemplar el caso en el que el valor no se encuentre en
el árbol. (en TAD)

03: Desarrollar la función copy, que devuelve una copia profunda del árbol actual (en TAD)

04: Desarrollar la función sin_hojas, que devuelva un nuevo árbol sin las hojas del
árbol actual.(En TAD)

05: Desarrollar la función recursiva ramas, que devuelve una lista de listas con
todas las ramas del árbol n-ario.

06: Desarrollar una función que devuelva una lista con los antecesores del dato
buscado en el árbol, contemplando la situación de que el dato pueda no existir
(devolver en este caso una lista vacia).
"""

from typing import Generic, TypeVar
from functools import reduce

T = TypeVar('T')

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []

    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])

    def __str__(self):
        def mostrar(t: ArbolN[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            out = indent + str(t.dato) + '\n'
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out
            
        return mostrar(self, 0)
    
    def __eq__(self, otro: "ArbolN[T]") -> bool:
        if self.dato != otro.dato:
            return False
        
        if len(self.subarboles) != len(otro.subarboles):
            return False
        
        return all([subarbol == otro.subarboles[i] for i, subarbol in enumerate(self.subarboles)])

    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> "list[ArbolN[T]]":
        return self._subarboles
    
    @subarboles.setter
    def subarboles(self, subarboles: "list[ArbolN[T]]"):
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: "ArbolN[T]"):
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        def altura_n(bosque: list[ArbolN[T]]) -> int:
            if not bosque:
                return 0
            else:
                return max(bosque[0].altura(), altura_n(bosque[1:]))
        
        return 1 + altura_n(self.subarboles)

    def preorder_funcional(self) -> list[T]:
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.preorder_funcional(), self.subarboles, [self.dato])

    def preorder_iterativa(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder_iterativa()
        return recorrido
    
    def preorder_recursiva(self) -> list[T]:
        def preorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            return [] if not bosque else bosque[0].preorder_recursiva() + preorder_n(bosque[1:])
        return [self.dato] + preorder_n(self.subarboles)

    def bfs(self) -> list[T]:
        """
        Recupera los datos del n-árbol en recorrido BFS. Iterativa.
        """
        recorrido = []
        cola = [self]
        while cola:
            t = cola.pop(0)
            recorrido.append(t.dato)
            cola += t.subarboles
        return recorrido
    
    def posorder_recursiva(self) -> list[T]:
        """
        Recupera los datos del n-árbol en recorrido posorder. Recursiva.
        """
        def posorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            if not bosque:
                return []
            else:
                return bosque[0].posorder_recursiva() + posorder_n(bosque[1:])
        return posorder_n(self.subarboles) + [self.dato]
    
    def posorder_iterativa(self) -> list[T]:
        """
        Recupera los datos del n-árbol en recorrido posorder. Iterativa.
        """
        recorrido = []
        cola = [self]
        while cola:
            t = cola.pop()
            recorrido.append(t.dato)
            cola += t.subarboles
        return recorrido[::-1]

    def posorder_funcional(self) -> list[T]:
        """
        Recupera los datos del n-árbol en recorrido posorder. Funcional.
        """
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.posorder_funcional(), self.subarboles, []) + [self.dato]

    def nivel(self, x: T) -> int:
        """
        Devuelve el nivel de un dato en el árbol.
        Si el dato no se encuentra en el árbol, devuelve -1.
        """
        def nivel_n(bosque: list[ArbolN[T]], x: T, nivel: int) -> int:
            if not bosque: # Sin subarboles, no se encontró el dato.
                return -1
            elif bosque[0].dato == x: # Se encontró el dato.
                return nivel + 1
            else: # De todos los niveles encontrados, devolver el mayor.
                return max(nivel_n(bosque[1:], x, nivel), nivel_n(bosque[0].subarboles, x, nivel + 1))
        
        return nivel_n(bosque=self.subarboles, x=x, nivel=1)
    
    def copy(self) -> "ArbolN[T]":
        """
        Devuelve una copia profunda del árbol.
        """
        arbol = ArbolN(self.dato)
        arbol.subarboles = [subarbol.copy() for subarbol in self.subarboles]
        return arbol
        
    def sin_hojas(self) -> "ArbolN[T]":
        """
        Devuelve un nuevo árbol sin las hojas del árbol actual.
        """
        if not self.subarboles: # Si no tiene subarboles, es hoja.
            return ArbolN(self.dato)
        else: # Si tiene subarboles, no es hoja.
            arbol = ArbolN(self.dato)
            # Recursivamente, obtener los subarboles sin hojas.
            arbol.subarboles = [subarbol.sin_hojas() for subarbol in self.subarboles if not subarbol.es_hoja()]
            return arbol
    
    def rama(self) -> list[list[T]]:
        """
        Devuelve una lista de listas con todas las ramas del árbol n-ario.
        El algoritmo obtiene las ramas de los subarboles y las concatena con el dato del árbol actual.
        """
        ramas = []
        if self.es_hoja():
            return [[self.dato]]
        else:
            for subarbol in self.subarboles:
                for rama in subarbol.rama():
                    ramas.append([self.dato] + rama)
            return ramas
    
    def antecesores(self, valor: T) -> list[T]:
        """
        Devuelve una lista con los antecesores del dato buscado en el árbol.
        Si el dato no existe, devuelve una lista vacía.
        """
        def antecesores_n(bosque: list[ArbolN[T]], valor: T, antecesores: list[T]) -> list[T]:
            if not bosque:
                return []
            elif bosque[0].dato == valor:
                return antecesores
            else:
                # Buscar en los subarboles del bosque actual
                # Si no se encuentra en el subarbol actual, buscar en el resto del bosque.
                return \
                    antecesores_n(bosque=bosque[0].subarboles, valor=valor, antecesores=antecesores + [bosque[0].dato]) \
                    or antecesores_n(bosque=bosque[1:], valor=valor, antecesores=antecesores)
        
        return antecesores_n(bosque=[self], valor=valor, antecesores=[])

    # def recorrido_guiado(self, direcciones: list[int]) -> T:
    #     pass


def main():
    t = ArbolN(1)
    n2 = ArbolN(2)
    n3 = ArbolN(3)
    n4 = ArbolN(4)
    n5 = ArbolN(5)
    n6 = ArbolN(6)
    n7 = ArbolN(7)
    n8 = ArbolN(8)
    n9 = ArbolN(9)
    t.insertar_subarbol(n2)
    t.insertar_subarbol(n3)
    t.insertar_subarbol(n4)
    n2.insertar_subarbol(n5)
    n2.insertar_subarbol(n6)
    n4.insertar_subarbol(n7)
    n4.insertar_subarbol(n8)
    n7.insertar_subarbol(n9)
    
    print(t)

    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(f'BFS: {t.bfs()}')

    print(f'DFS preorder (funcional): {t.preorder_funcional()}')
    print(f'DFS preorder (iterativa): {t.preorder_iterativa()}')
    print(f'DFS preorder (recursiva): {t.preorder_recursiva()}')

    print(f'DFS posorder (funcional): {t.posorder_funcional()}')
    print(f'DFS posorder (iterativa): {t.posorder_iterativa()}')
    print(f'DFS posorder (recursiva): {t.posorder_recursiva()}')

    print(f'Nivel de 9: {t.nivel(9)}')
    print(f'Nivel de 13: {t.nivel(13)}')
    print(f'Nivel de 2: {t.nivel(2)}')

    t2 = t.copy()
    t3 = t2.sin_hojas()
    print(t)
    print(t2)
    print(t3)
    print(f't == t2 {t == t2}')
    print(f't == t3 {t == t3}')

    print(f'Ramas: {t.rama()}')

    print(f'Antecesores de 9: {t.antecesores(9)}')
    print(f'Antecesores de 13: {t.antecesores(13)}')
    print(f'Antecesores de 1: {t.antecesores(1)}')

    # print(f'recorrido_guiado [2,0,0]: {t2.recorrido_guiado([2,0,0])}')


if __name__ == '__main__':
    main()
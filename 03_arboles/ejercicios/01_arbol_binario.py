"""
Ejercicio 01
Crear dentro del TAD ArbolBinario una función recursiva nivel, que dado un valor, retorne en
qué nivel se encuentra en el nodo del árbol. Si el valor no se encontrara en el árbol, retornar un
valor superior a la altura del árbol.

Ejercicio 02
Desarrollar dentro del TAD ArbolBinario una función recursiva copy, que devuelva la deep copy
de un árbol (el prototipo se encuentra en el template)
"""

from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self):
        return self.dato
    
class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None
        
    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs)
            return wrapper
        
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.si
    
    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.sd
    
    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio
    def dato(self) -> T:
        assert self.raiz is not None
        return self.raiz.dato
    
    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si

    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo
        
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)

    # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    def inorder(self) -> list[T]:
        """
        Using stack recursion
        """
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()
    
    def inorder_tail(self) -> list[T]:
        """
        Like inorder method, but using tail recursion
        """
        def _inorder(t: ArbolBinario[T], acc: list[T]) -> list[T]:
            if t.es_vacio():
                return acc
            else:
                acc = _inorder(t.si(), acc)
                acc.append(t.dato())
                return _inorder(t.sd(), acc)
        
        return _inorder(self, [])

    def preorder(self) -> list[T]:
        def _preorder(t: ArbolBinario[T], acc: list[T]) -> list[T]:
            if t.es_vacio():
                return acc
            else:
                return _preorder(t.sd(), _preorder(t.si(), acc + [t.dato()]))
    
        return _preorder(self, [])
        

    def posorder(self) -> list[T]:
        def _posorder(t: ArbolBinario[T], acc: list[T]) -> list[T]:
            if t.es_vacio():
                return acc
            else:
                return _posorder(t.si(), _posorder(t.sd(), [t.dato()] + acc))
        
        return _posorder(self, [])

    def bfs(self) -> list[T]:
        """
        https://www.geeksforgeeks.org/level-order-tree-traversal/
        """
        if self.es_vacio():
            return []
        else:
            cola = [self]
            out = []
            while len(cola) > 0:
                t = cola.pop(0)
                out.append(t.dato())
                if not t.si().es_vacio():
                    cola.append(t.si())
                if not t.sd().es_vacio():
                    cola.append(t.sd())
            return out

    def nivel(self, x: T) -> int:
        def _nivel(t: ArbolBinario[T], x: T, nivel: int) -> int:
            if t.es_vacio():
                return nivel + 1
            elif t.dato() == x:
                return nivel
            else:
                return max(_nivel(t.si(), x, nivel + 1), _nivel(t.sd(), x, nivel + 1))
        
        return _nivel(self, x, 0)

    def copy(self) -> "ArbolBinario[T]":
        def _copy(t: ArbolBinario[T]) -> ArbolBinario[T]:
            if t.es_vacio():
                return ArbolBinario()
            else:
                return ArbolBinario.crear_nodo(t.dato(), _copy(t.si()), _copy(t.sd()))
        
        return _copy(self)

    def espejo(self) -> "ArbolBinario[T]":
        def _espejo(t: ArbolBinario[T]) -> ArbolBinario[T]:
            if t.es_vacio():
                return ArbolBinario()
            else:
                return ArbolBinario.crear_nodo(t.dato(), _espejo(t.sd()), _espejo(t.si()))
        
        return _espejo(self)
        
    def sin_hojas(self):
        def _sin_hojas(t: ArbolBinario[T]) -> ArbolBinario[T]:
            if t.es_vacio():
                return ArbolBinario()
            elif t.es_hoja():
                return ArbolBinario()
            else:
                return ArbolBinario.crear_nodo(t.dato(), _sin_hojas(t.si()), _sin_hojas(t.sd()))
        
        return _sin_hojas(self)
        

def main():
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(60)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)
    
    print(t)

    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(f'BFS: {t.bfs()}')

    t2 = t.copy()
    print(t)
    print(f'DFS inorder stack: {t.inorder()}')
    print(f'DFS inorder tail:  {t2.inorder_tail()}')
    print(f'Nivel de 8: {t2.nivel(8)}')

    t3 = t2.espejo()
    print(t3)
    print(t3.sin_hojas())


if __name__ == '__main__':
    main()
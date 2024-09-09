from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig = Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        elif self._head is not None:
            return self._head.dato
        else:
            raise AttributeError('`dato` no es un atributo de None')

    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        elif self._head is not None:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self.head()), parcial)
            return actual
        else:
            raise AttributeError('`sig` no es un atributo de None')
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        elif self._head is not None:
            return self._head.sig.copy()
        else:
            raise AttributeError('`sig` no es un atributo de None')

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig # type: ignore
                else:
                    _eliminar_interna(actual._head.sig, actual, valor) # type: ignore

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head # type: ignore
            else:
                _eliminar_interna(self._head.sig, self, valor) # type: ignore

    def ultimo(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        elif self._head is not None:
            if self._head.sig.es_vacia():
                return self.head()
            else:
                return self._head.sig.ultimo()
        else:
            raise AttributeError('`sig` no es un atributo de None')

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        if self.es_vacia():
            return ys
        else:
            actual = self.copy()
            if self._head.sig is not None: # type: ignore
                actual._head.sig = self._head.sig.concat(ys) # type: ignore
            else:
                actual._head.sig = ys # type: ignore
            return actual
        
    def join(self, separador: str = '') -> str:
        if self.es_vacia():
            return ''
        else:
            if self.tail().es_vacia():
                return f'{self.head()}'
            else:
                return f'{self.head()}{separador}{self.tail().join(separador)}'
        
    def index(self, valor: T) -> int:
        def _index_interna(actual: ListaGenerica, valor: T, index: int):
            if actual.es_vacia():
                return -1
            elif actual.head() == valor:
                return index
            else:
                return _index_interna(actual.tail(), valor, index + 1)
            
        return _index_interna(self, valor, 0)
        
    def existe(self, valor: T) -> bool:
        resultado = self.index(valor=valor)
        return resultado != -1

    def __len__(self):
        if self.es_vacia():
            return 0
        else:
            return 1 + self.tail().__len__()
    
    def __getitem__(self, index = None): # No cubre el caso de slicing
        if index == None:
            raise IndexError("No pasaste un index")
        elif self._head is not None:
            if index == 0:
                return self.head()
            else:
                return self.tail().__getitem__(index=index - 1)
        else:
            raise IndexError("Te pasaste del largo de la lista")

    def __repr__(self):
        if self.es_vacia():
            return 'Vacía'
        else:
            if self.tail().es_vacia():
                return f'[{self.head()}]'
            else:
                return f'[{self.join(", ")}]'
        
    def __eq__(self, otra: ListaGenerica) -> bool:
        if not isinstance(otra, Lista): # type: ignore
            return False
        if len(self) != len(otra):
            return False
        if self.es_vacia():
            return True
        if self.head() != otra.head():
            return False
        return self.tail() == otra.tail()

if __name__ == '__main__':
    xs: Lista[int] = Lista()
    
    print(f'xs es vacia? {xs.es_vacia()}')	# True
    
    # Operaciones basicas
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)
    
    print(f'xs: {xs}')						# [20, 10, 4]
    print(f'ys: {ys}')						# [8, 9, 4]
    print(f'xs es vacia? {xs.es_vacia()}')	# False
    print(f'ultimo(xs): {xs.ultimo()}')		# 4
    print(f'len(xs): {len(ys)}')			# 3, ver __len__
    print(f'xs[1]: {xs[1]}')				# 10, ver __getitem__
    # print(f'xs[10]: {xs[10]}')				# Error, ver __getitem__

    # Consumiendo como iterable
    for x in xs:
        print(x)	# 20 -> 10 -> 4

    # Otras operaciones
    print(f'xs.concat(ys): {xs.concat(ys)}')		# [20, 10, 4, 8, 9, 4]
    print(f'cat de listas vacias: {Lista().concat(Lista())}')	# Vacía
    print(f'xs.concat(Lista()): {xs.concat(Lista())}')		# [20, 10, 4]
    print(f'Lista().concat(xs): {Lista().concat(xs)}')		# [20, 10, 4]

    print(f'ys.join(" -> "): {ys.join(" -> ")}')	# 8 -> 9 -> 4
    print(f'xs.index(4): {xs.index(4)}')			# 2
    print(f'xs.index(423): {xs.index(423)}')			# -1
    print(f'xs.existe(10): {xs.existe(10)}')        # True
    print(f'xs.existe(100): {xs.existe(100)}')        # False
    print(f'xs == zs? {xs == zs}')                  # False
    zs.insertar(10)
    zs.insertar(20)
    print(f'xs == zs? {xs == zs}')                  # True
    
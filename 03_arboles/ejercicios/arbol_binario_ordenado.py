"""
Ejercicios

01: Implementar los dunder methods restantes en la clase NodoABO

02: Mejorar el algoritmo de inserción para que no admita elementos repetidos.

03: Desarrollar la función pertenece que se encuentra en el TAD respetando su firma.

04: Desarrollar el algoritmo de búsqueda de un árbol binario de búsqueda, que
devuelva True si el valor proporcionado fue encontrado o, caso contrario, False.

05: Desarrollar la función recursiva minimo que devuelva el valor mínimo del
Árbol Binario Ordenado, en caso de existir.

06: Desarrollar una función recursiva valores_menor_a que, dado un valor,
devuelva una lista con todos los valores menores a ese valor proporcionado

07: Desarrollar una función recursiva recorrer_mayor_menor que devuelva una
lista con los valores contenidos en el árbol binario ordenado de mayor a menor

08: Desarrollar la función recursiva con la siguiente firma: encontrar_max(self,
arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]", que
encuentra y devuelve el subárbol que tiene el valor máximo en su raíz

09: Desarrollar la función recursiva con la siguiente firma: encontrar_min(self,
arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]", que
encuentra y devuelve el subárbol que tiene el valor mínimo en su raíz.

10: Desarrollar ambos algoritmos recursivos de eliminación (por fusión y copia)
de un árbol binario de búsqueda. Incluir los casos triviales dentro de ellos.
En caso de que el valor a eliminar no se encuentre en el árbol, no se debe
realizar ninguna acción.
"""

from typing import TypeVar, Optional, Protocol
from arbol_binario import ArbolBinario, NodoAB

_Decoradores = ArbolBinario._Decoradores

class Comparable(Protocol):
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)


class NodoABO(NodoAB[T]):
    def __init__(self, dato: T):
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())
    
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato
    
    def __le__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato <= otro.dato

    def __ge__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato >= otro.dato
    
    def __ne__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato != otro.dato
    
    def __repr__(self) -> str:
        return f"NodoABO({self.dato})"
    
    def __str__(self) -> str:
        return str(self.dato)
    
    def __hash__(self) -> int:
        return hash(self.dato)
    
    
class ArbolBinarioOrdenado(ArbolBinario[T]):
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    @staticmethod
    def convertir_ordenado(arbol_binario: ArbolBinario[T]) -> "ArbolBinarioOrdenado[T]":
        if arbol_binario.es_vacio():
            return ArbolBinarioOrdenado()
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(arbol_binario.dato()))
        nuevo.insertar_si(ArbolBinarioOrdenado.convertir_ordenado(arbol_binario.si()))
        nuevo.insertar_sd(ArbolBinarioOrdenado.convertir_ordenado(arbol_binario.sd()))
        return nuevo
    
    def es_ordenado(self) -> bool:
        def es_ordenado_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
            minimo: Optional[T] = None, 
            maximo: Optional[T] = None
        ) -> bool:
            if arbol.es_vacio():
                return True
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)
        
        return es_ordenado_interna(self)
    
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()
        super().insertar_si(arbol)
        if not self.es_ordenado():
            super().insertar_si(si)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()
        super().insertar_sd(arbol)
        if not self.es_ordenado():
            super().insertar_sd(sd)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar(self, valor: T):
        if self.es_vacio():
            self.set_raiz(NodoABO(valor))
        elif valor < self.dato():
            self.si().insertar(valor)
        elif valor > self.dato():
            self.sd().insertar(valor)
        else:
            raise ValueError("No se admiten elementos repetidos")

    def pertenece(self, valor: T) -> bool:
        if self.es_vacio():
            return False
        elif valor == self.dato():
            return True
        else:
            return self.si().pertenece(valor) or self.sd().pertenece(valor)

    def buscar(self, valor: T) -> bool: # Consultar: no es lo mismo que pertenece?
        if self.es_vacio():
            return False
        if valor == self.dato():
            return True
        if valor < self.dato():
            return self.si().buscar(valor)
        return self.sd().buscar(valor)

    @_Decoradores.valida_es_vacio
    def minimo(self) -> Optional[T]:
        if self.si().es_vacio():
            return self.dato()
        return self.si().minimo()
    
    @_Decoradores.valida_es_vacio
    def maximo(self) -> Optional[T]:
        if self.sd().es_vacio():
            return self.dato()
        return self.sd().maximo()
    
    def valores_menor_a(self, valor: T) -> list[T]:
        if self.es_vacio():
            return []
        if self.dato() < valor:
            return [self.dato()] + self.si().valores_menor_a(valor) + self.sd().valores_menor_a(valor)
        return self.si().valores_menor_a(valor)
    
    def recorrer_mayor_menor(self) -> list[T]:
        if self.es_vacio():
            return []
        return self.sd().recorrer_mayor_menor() + [self.dato()] + self.si().recorrer_mayor_menor()
    
    @_Decoradores.valida_es_vacio
    def encontrar_max(self, arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]":
        if arbol.sd().es_vacio():
            return arbol
        return self.encontrar_max(arbol.sd())
    
    @_Decoradores.valida_es_vacio
    def encontrar_min(self, arbol: "ArbolBinarioOrdenado[T]") -> "ArbolBinarioOrdenado[T]":
        if arbol.si().es_vacio():
            return arbol
        return self.encontrar_min(arbol.si())
    
    @_Decoradores.valida_es_vacio
    def eliminar_por_fusion(self, valor: T) -> "ArbolBinarioOrdenado[T]":
        if not self.pertenece(valor):
            return self
        if valor < self.dato():
            self.insertar_si(self.si().eliminar_por_fusion(valor))
        elif valor > self.dato():
            self.insertar_sd(self.sd().eliminar_por_fusion(valor))
        else: # valor == self.dato()
            # Casos triviales
            if self.es_hoja():
                return ArbolBinarioOrdenado()
            elif self.si().es_vacio():
                return self.sd()
            elif self.sd().es_vacio():
                return self.si()
            else: # Caso no trivial
                arbol_max = self.encontrar_max(self.si()) # Buscar el máximo en el subárbol izquierdo
                arbol_max.insertar_sd(self.sd()) # Fusionar el subárbol derecho del árbol actual con el máximo del subárbol izquierdo
                self.set_raiz(self.si().raiz) # Reemplazar la raíz del árbol actual por la raíz del subárbol izquierdo
        return self
        

def main():
    t: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado() # type: ignore
    t.insertar(10)
    t.insertar(5)
    t.insertar(15)
    t.insertar(2)
    t.insertar(7)
    t.insertar(12)
    t.insertar(17)
    t.insertar(20)
    t.insertar(13)
    # print(t.es_ordenado())
    # print(t)

    t2: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado() # type: ignore
    t2.insertar(8)
    # t2.insertar(8) # Descomentar para probar que no se admiten elementos repetidos
    # t2.insertar(11)   # Descomentar para probar la excepción al violar el orden
    t2.insertar(6)
    t.insertar_si(t2)
    # print(t)
    print(f'Ordenado?: {t.es_ordenado()}') # True

    print(f'Tiene 12?: {t.pertenece(12)}') # True
    print(f'Tiene 14?: {t.pertenece(14)}') # False

    print(f'Busca 12?: {t.buscar(12)}') # True
    print(f'Busca 14?: {t.buscar(14)}') # False

    print(f'Mínimo: {t.minimo()}')

    print(f'Valores menores a 15: {t.valores_menor_a(15)}')

    print(f'Recorrido de mayor a menor: {t.recorrer_mayor_menor()}')

    # print(t)
    # print(f'Encontrar máximo: \n{t.encontrar_max(t.sd())}')
    # print(f'Encontrar mínimo: \n{t.encontrar_min(t.sd())}')

    # print(t)
    # print(f'Eliminar 8: \n{t.eliminar_por_fusion(8)}') # Sin subárbol derecho
    # print(f'Eliminar 15: \n{t.eliminar_por_fusion(15)}') # Sin subárbol izquierdo
    # print(f'Eliminar 10: \n{t.eliminar_por_fusion(10)}') # Con ambos subárboles

if __name__ == "__main__":
    main()
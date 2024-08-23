"""
ACLARACION: Este ejercicio lo hice con type hints. No es necesario que lo hagan con type hints.

Una cadena de restaurantes llamada "Delicioso Sabor" desea implementar un sistema de gestión de pedidos
automatizado para mejorar la eficiencia en el manejo de sus ventas y optimizar el control de su inventario.
Requerimientos del Sistema:
    1. Clase Producto:
        ○ Cada producto en el menú del restaurante debe ser representado por la clase Producto.
        ○ Los productos deben tener un nombre, precio unitario y cantidad inicial en stock.
        ○ Se debe poder actualizar la cantidad en stock de cada producto conforme se realicen pedidos.
    2. Clase Pedido:
        ○ La clase Pedido debe registrar los detalles de cada pedido realizado por los clientes.
        ○ Cada pedido debe contener un número único de identificación, una lista de productos solicitados y su
        estado actual.
        ○ Se debe calcular el costo total del pedido, aplicando un descuento global del 10% por defecto.
        ○ Se debe poder actualizar el estado de los pedidos a medida que progresan en su preparación y
    entrega.
"""

from typing import Literal, TypedDict

Estado = Literal["en_proceso", "finalizado"]

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad = 0) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def sumar_stock(self, cantidad: int) -> None:
        self.cantidad += cantidad
    
    def reducir_stock(self, cantidad: int) -> None:
        self.cantidad -= cantidad


class ProductoEntidad(TypedDict):
    nombre: str
    precio: float
    cantidad: int


class Pedido:
    pedido_id = 1
    descuento = 0.9
    def __init__(self) -> None:
        self.id = Pedido.pedido_id
        self.productos: list[ProductoEntidad] = []
        self.estado_actual: Estado = "en_proceso"
        Pedido.pedido_id += 1
    
    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if (producto.cantidad < cantidad):
            raise Exception("Not enough stock")

        producto_idx = None

        for idx, p in enumerate(self.productos):
            if p["nombre"] == producto.nombre:
                producto_idx = idx
        
        if producto_idx == None:
            self.productos.append({
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": cantidad
            })
        else:
            self.productos[producto_idx]["cantidad"] += cantidad

        producto.reducir_stock(cantidad=cantidad)
    
    def obtener_costo(self) -> float:
        total =  sum([p["precio"] * p["cantidad"] for p in self.productos])
        self.estado_actual = "finalizado"
        return total * Pedido.descuento
    

if __name__ == "__main__":
    coca = Producto(nombre="Manaos Cola", precio=850, cantidad=100)
    fanta = Producto(nombre="Fanta", precio=1200, cantidad=100)
    fernet = Producto(nombre="Fernandito", precio=500, cantidad=200)

    pedido_1 = Pedido()
    pedido_1.agregar_producto(producto=coca, cantidad=7)
    pedido_1.agregar_producto(producto=fernet, cantidad=3)
    pedido_1.agregar_producto(producto=coca, cantidad=3)

    print(pedido_1.obtener_costo())
    print(coca.cantidad)
    print(fernet.cantidad)

    pedido_2 = Pedido()

    print(pedido_1.id, pedido_2.id)

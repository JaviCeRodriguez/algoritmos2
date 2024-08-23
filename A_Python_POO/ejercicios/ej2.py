"""
Implemente una clase Monedero que permita gestionar la cantidad de dinero que
una persona dispone en un momento dado. La clase deberá tener un constructor
que permitirá crear un monedero con una cantidad de dinero inicial y deberá
definir un método para meter dinero en el monedero, otro para sacarlo y
finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de
dinero del monedero a través de este último método. Por supuesto, no se podrá
sacar más dinero del que haya en un momento dado en el monedero.
"""

class Monedero:
    def __init__(self, cantidad_inicial):
        self.cantidad = cantidad_inicial
    
    def meter_dinero(self, cantidad):
        self.cantidad += cantidad
    
    def sacar_dinero(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print("No hay suficiente dinero en el monedero")
    
    def consultar_disponible(self):
        print(f"El monedero tiene ${self.cantidad}")

if __name__ == '__main__':
    monedero = Monedero(100)
    monedero.consultar_disponible()
    monedero.meter_dinero(50)
    monedero.consultar_disponible()
    monedero.sacar_dinero(200)
    monedero.sacar_dinero(50)
    monedero.consultar_disponible()
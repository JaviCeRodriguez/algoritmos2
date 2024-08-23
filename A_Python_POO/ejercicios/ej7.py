"""
a) Crear una clase Vehiculo con los siguientes atributos y métodos:
    ● Atributos:
        ○ marca (String)
        ○ modelo (String)
        ○ precioBase (double).
    ● Métodos:
        ○ Un constructor que acepte la marca, modelo y precio base del vehículo.
        ○ Un método calcularCostoAlquiler(int dias) que calcule el costo de alquiler del vehículo
        durante el número de días especificado. El costo se calcula como precioBase * dias.

b) Crear dos subclases Auto y Moto, que hereden de la clase Vehiculo. Las subclases deben incluir
un constructor que llame al constructor de la superclase y también deben sobrescribir el método
calcularCostoAlquiler(int dias) de la siguiente manera:
    ● Para Auto, el costo de alquiler se calcula incrementando un 20% el costo común.
    ● Para Moto, el costo de alquiler se calcula con un descuento del 15% respecto al vehículo.
"""

class Vehiculo:
    def __init__(self, marca: str, modelo: str, precio_base: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precio_base = precio_base
    
    def calcular_costo_alquiler(self, dias: int) -> float:
        return self.precio_base * dias
    
class Auto(Vehiculo):
    incremento = 1.2
    def __init__(self, marca: str, modelo: str, precio_base: float) -> None:
        super().__init__(marca, modelo, precio_base)
    
    def calcular_costo_alquiler(self, dias: int) -> float:
        return super().calcular_costo_alquiler(dias) * Auto.incremento
    
class Moto(Vehiculo):
    descuento = 0.85
    def __init__(self, marca: str, modelo: str, precio_base: float) -> None:
        super().__init__(marca, modelo, precio_base)
    
    def calcular_costo_alquiler(self, dias: int) -> float:
        return super().calcular_costo_alquiler(dias) * Moto.descuento
    
if __name__ == "__main__":
    auto = Auto("Ford", "Focus", 1000)
    moto = Moto("Yamaha", "FZ", 500)
    
    print(auto.calcular_costo_alquiler(5))
    print(moto.calcular_costo_alquiler(5))

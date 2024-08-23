"""
La cadena de restaurantes "Delicias del Mar" desea mejorar su sistema de gestión de sus sucursales i
Requerimientos Funcionales:
    1. Clase Restaurante:
        ○ Definir una clase llamada Restaurante que contenga como atributos: nombre del restaurante, ciudad
        donde se encuentra y número de empleados.
        ○ Implementar un métodoobtener_numero_sucursales() que retorne el número total de sucursales de la
        cadena.
        ○ Implementar un método calcular_costo_operativo(empleado_promedio) que calcule el costo
        mensual de operación de una sucursal. Considerar un salario promedio mensual por empleado de $2000.

Crear instancias de la clase Restaurante para representar diferentes sucursales con sus respectivos nombres,
ciudades y número de empleados.

Usar el método obtener_numero_sucursales() para obtener y mostrar el número total de sucursales de la cadena.

Usar el método calcular_costo_operativo() para calcular y mostrar el costo mensual de operación de cada
sucursal creada.
"""

class Restaurante:
    sucursales = 0
    salario = 2000

    def __init__(self, nombre: str, ciudad: str, empleados: int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
        Restaurante.sucursales += 1

    @classmethod
    def _numero_sucursales(cls) -> int:
        return cls.sucursales
    
    def calcular_costo_operativo(self) -> int:
        return self.empleados * Restaurante.salario


if __name__ == "__main__":
    chef_pepita = Restaurante(nombre="Las delicias de Pepita", ciudad="Mar del Plata", empleados=200)
    chefcito = Restaurante(nombre="Ratatouille", ciudad="París", empleados=15)

    print("Número de sucursales", Restaurante._numero_sucursales())
    print(f"Costo operativo de {chef_pepita.nombre}: ${chef_pepita.calcular_costo_operativo()}")
    print(f"Costo operativo de {chefcito.nombre}: ${chefcito.calcular_costo_operativo()}")
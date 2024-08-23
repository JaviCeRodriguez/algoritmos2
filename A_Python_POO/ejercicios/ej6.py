"""
Implemente la clase Fecha, que permita representar una terna de día, mes y año,
todos de tipo entero. Programar un método que determine si una fecha es mayor
a otra. Programar la sobrecarga del método __str__ y __gt__(operador mayor).
"""

class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.anio}"
    
    def __gt__(self, otra_fecha: "Fecha") -> bool:
        return (self.anio, self.mes, self.dia) > (otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)


if __name__ == '__main__':
    fecha1 = Fecha(1, 1, 2021)
    fecha2 = Fecha(1, 1, 2022)
    print(f"La fecha {fecha1} es {'mayor' if fecha1 > fecha2 else 'menor'} que la fecha {fecha2}")
    fecha3 = Fecha(1, 2, 2021)
    print(f"La fecha {fecha1} es {'mayor' if fecha1 > fecha3 else 'menor'} que la fecha {fecha3}")
    fecha4 = Fecha(2, 1, 2021)
    print(f"La fecha {fecha1} es {'mayor' if fecha1 > fecha4 else 'menor'} que la fecha {fecha4}")
    fecha5 = Fecha(1, 1, 2021)
    print(f"La fecha {fecha1} es {'mayor' if fecha1 > fecha5 else 'menor'} que la fecha {fecha5}")
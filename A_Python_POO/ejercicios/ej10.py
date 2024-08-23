"""
Definir la clase Automovil, que puede subclasificarse en AutoMediano o Camion.
Los autos medianos son capaces de estar habilitados luego de la adquisición de
un permiso en una fecha dada. Los camiones también podrán estar habilitados
luego de la adquisición de un permiso, pero éste sólo podrá expedirse con la
debida autorización previa de la concesionaria donde fue adquirido. Las
concesionarias de camiones verifican ciertas características del camión para
poder registrar al mismo. Este dato también es registrado dentro de la misma
concesionaria.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Automovil(ABC):
    def __init__(self, brand, model, year, license_plate):
        self.brand = brand
        self.model = model
        self.year = year
        self.license_plate = license_plate

    @abstractmethod
    def enabled(self):
        pass

class AutoMediano(Automovil):
    def __init__(self, brand, model, year, license_plate, permit_date):
        super().__init__(brand, model, year, license_plate)
        self.permit_date = datetime.strptime(permit_date, "%Y-%m-%d")

    def enabled(self, current_date):
        current_date = datetime.strptime(current_date, "%Y-%m-%d")
        return self.permit_date >= current_date
    
class Camion(Automovil):
    def __init__(self, brand, model, year, license_plate, dealership_authorization, features):
        super().__init__(brand, model, year, license_plate)
        self.dealership_authorization = dealership_authorization
        self.features = features
    
    def enabled(self, dealership):
        return self.dealership_authorization == dealership

if __name__ == "__main__":
    auto = AutoMediano(brand="Ford", model="Fiesta", year=2015, license_plate="ABC123", permit_date="2022-01-01")
    truck = Camion(brand="Scania", model="R450", year=2020, license_plate="DEF456", dealership_authorization="Scania", features="Max load 30 tons")

    print(auto.enabled(current_date="2022-01-01"))
    print(auto.enabled(current_date="2023-01-01"))
    print(truck.enabled(dealership="Scania"))
    print(truck.enabled(dealership="Mercedes Benz"))

"""
Implemente la clase Hora que contenga miembros datos separados para almacenar
horas, minutos y segundos. Un constructor inicializará estos datos en 0 y otro a valores
dados. Una función miembro deberá visualizar la hora en formato hh:mm:ss. Otra
función miembro sumará dos objetos de tipo hora, retornando la hora resultante.
Realizar otra versión de la suma que asigne el resultado de la suma en el primer objeto
hora.
b) Programar un procedimiento main(), que cree dos horas inicializadas y uno que no lo
esté. Se deberán sumar los dos objetos inicializados, dejando el resultado en el objeto
no inicializado. Por último, se pide visualizar el valor resultante.
"""

class Hora:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def add(self, other_time: "Hora") -> "Hora":
        seconds = self.seconds + other_time.seconds
        minutes = self.minutes + other_time.minutes
        hours = self.hours + other_time.hours

        if seconds >= 60:
            seconds -= 60
            minutes += 1

        if minutes >= 60:
            minutes -= 60
            hours += 1

        return Hora(hours, minutes, seconds)

    def add_inplace(self, other_time) -> None:
        self.seconds += other_time.seconds
        self.minutes += other_time.minutes
        self.hours += other_time.hours

        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

def main():
    time1 = Hora(10, 30, 45)
    time2 = Hora(2, 15, 30)
    time3 = Hora()

    print(f"Hora 1: {time1}")
    print(f"Hora 2: {time2}")
    print(f"Hora 3: {time3}")

    time3 = time1.add(time2)
    print(f"Hora 3: {time3}")

    time3 = Hora()
    time3.add_inplace(time1)
    time3.add_inplace(time2)
    print(f"Hora 3: {time3}")

if __name__ == "__main__":
    main()
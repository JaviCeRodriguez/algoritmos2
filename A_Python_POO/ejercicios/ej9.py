"""
Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases.
"""

class Publicacion:
    def __init__(self, titulo: str, precio: float) -> None:
        self.titulo = titulo
        self.precio = precio

class Libro(Publicacion):
    def __init__(self, titulo: str, precio: float, paginas: int, anio: int) -> None:
        super().__init__(titulo, precio)
        self.paginas = paginas
        self.anio = anio

class Disco(Publicacion):
    def __init__(self, titulo: str, precio: float, duracion: int) -> None:
        super().__init__(titulo, precio)
        self.duracion = duracion

if __name__ == "__main__":
    libro = Libro("El principito", 500, 100, 1943)
    disco = Disco("Thriller", 1000, 45)

    print(f"Libro: {libro.titulo}, {libro.paginas} páginas, {libro.anio}, ${libro.precio}")
    print(f"Disco: {disco.titulo}, {disco.duracion} minutos, ${disco.precio}")
    
"""
Definir la función quicksort, que dada una lista de
enteros, retorne la lista original, pero con sus
elementos ordenados, utilizando el método de 
ordenamiento quicksort
"""

def quicksort(lista: list[int], debug=False) -> list[int]:
    def quicksort_interna(lista: list[int]) -> list[int]:
        if not lista:
            return []
        else:
            pivote = lista[0] # Tomo el primer elemento de la lista como pivote
            resto_lista = lista[1:] # Resto de la lista sin el pivote
            menores = [x for x in resto_lista if x <= pivote] # Menores o iguales al pivote
            mayores = [x for x in resto_lista if x > pivote] # Mayores al pivote
            if debug:
                print(f"{str(pivote):^10} | {str(menores):^30} | {str(mayores):^30}")
            return quicksort_interna(menores) + [pivote] + quicksort_interna(mayores)

    if debug:
        print(f"{'Pivote':^10} | {'Menores o iguales':^30} | {'Mayores':^30}")

    return quicksort_interna(lista=lista)


if __name__ == '__main__':
    lista: list[int] = [14, -21, 6, 2, 56, 44, 20]
    print(quicksort(lista)) # [-21, 2, 6, 14, 20, 44, 56]
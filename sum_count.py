def sumuj_do(liczba):
    suma = 0
    for liczba in range(0, liczba + 1):
        suma += liczba
    return suma


def sumuj2_do(liczba):
    return sum([liczba for liczba in range(0, liczba + 1)])

def sumuj3_do(liczba):
    return (1 + liczba) / 2 * liczba

def sumuj4_do(liczba):
    return float(sum({liczba for liczba in range(0, liczba + 1)}))

print(sumuj_do(6), sumuj2_do(6),sumuj3_do(6), sumuj4_do(6))

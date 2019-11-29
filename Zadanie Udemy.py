
""" 1. Wykonam ćwiczenie dodawania wybranego przedziału liczby
od 0 do wybranej przez liczby przez użytkownika, zwróć wynik.
    2. Sprawdź, która metoda jest najszybsza"""
import time

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

def sumuj_do3(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

def sumuj_do4(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


def function_performance(func, how_many_times = 1, *arg):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum

print(function_performance(sumuj_do, 500, 500))
print(function_performance(sumuj_do2, 500, 500))
print(function_performance(sumuj_do3, 500, 500))
print(function_performance(sumuj_do4, 500, 500))
print(function_performance(sumuj_do5, 500, 500))

setContainer = {i for i in range(500)}
listContainer = [i for i in range(500)]

def is_element_in(value, container):
    if value in container:
        return True
    else:
        return False
print(function_performance(is_element_in, 500, 500, setContainer))
print(function_performance(is_element_in, 500, 500, listContainer))


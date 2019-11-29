""" Wykonam ćwiczenie dodawania wybranego przedziału liczby
od 0 do wybranej przez użytkownika, plus program zwróci wynik"""
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

"""
start = time.perf_counter()
print(sumuj_do(liczba))
end = time.perf_counter()
print(end - start)
"""

def function_performance(func, how_many_times = 1, *arg):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum

print(function_performance(sumuj_do, 50000, 50000))
print(function_performance(sumuj_do2, 50000, 50000))
print(function_performance(sumuj_do3, 50000, 50000))
print(function_performance(sumuj_do4, 50000, 50000))
print(function_performance(sumuj_do5, 50000, 50000))




setContainer = {i for i in range(1000000)}
listContainer = [i for i in range(1000000)]


def is_element_in(value, container):
    if value in container:
        return True
    else:
        return False
print(function_performance(is_element_in, 15000, 80000, setContainer))
print(function_performance(is_element_in, 15000, 80000, listContainer))
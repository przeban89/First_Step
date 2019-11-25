""" Wykonam ćwiczenie dodawania wybranego przedziału liczby
od 0 do wybranej przez użytkownika, plus zwróci wynik"""

while(True):
    liczba = int(input("Podaj liczbę: "))
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

    print(sumuj_do(liczba))
    print(sumuj_do2(liczba))
    print(sumuj_do3(liczba))
    print(sumuj_do4(liczba))
    print(sumuj_do5(liczba))
    break


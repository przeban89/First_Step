import Definition
while(True):
    wybor = input(""" Wybierz jedną z poniższych opcji:
    1. Pole koła
    2. Pole trapezu
    3. Pole prostokąta
    4. Poke trójkąta
    5. Pole kwadratu
    6. Pole walca
    Jaki jest Twój wybór?: """)

    if (wybor == "1"):
        r = float(input("Podaj promień koła: "))
        print(round(Definition.pole_kola(r), 2))
    elif (wybor == "2"):
        a = float(input("Podaj długość podstawy trapezu: "))
        b = float(input("Podaj długoś górnej podstawy trapezu: "))
        h = float(input("Podaj wysokość trapezu: "))
        print(round(Definition.pole_trepezu(a,b,h), 2), "j^2")
    elif (wybor == "3"):
        a = float(input("Podaj długość boku prostokąta: "))
        b = float(input("Podaj szerokość prostokąta: "))
        print(round(Definition.pole_prostokata(a, b), 2))
    elif (wybor == "4"):
        a = float(input("Podaj długość boku trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        print(round(Definition.pole_trojkata(a, h), 2))
    elif (wybor == "5"):
        a = float(input("Podaj długość boku kwadratu: "))
        print(round(Definition.pole_kwadratu(a), 2), "j^2")
    elif (wybor == "6"):
        r = float(input("Podaj promień podstawy walca: "))
        h = float(input("Podaj wysokość walca: "))
        print(round(Definition.pole_walca(r,h), 2))
    else:
        print("Wprowadziłeś złą wartość spróbuj raz jeszcze")
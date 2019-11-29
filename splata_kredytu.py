import Definition
while(True):
    k = float(input("Podaj kwotę kredytu: "))
    o = float(input("Podaj oprocentowanie: "))
    m = float(input("Podaj liczbę miesięcy kredytowania: "))
    x = Definition.splata(k, o, m)
    print("Kwota kapitałowa do spłaty: ", round(x, 2))

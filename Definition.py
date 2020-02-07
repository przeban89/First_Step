import math

def pole_kola(r):
    return math.pi * r ** 2

def pole_trepezu(a, b, h):
    return (a + b) * h / 2

def pole_prostokata(a, b):
    return a * b

def pole_trojkata(a, h):
    return (a * h) / 2

def pole_kwadratu(a):
    return (a ** 2)

def pole_walca(r, h):
    return 2 * math.pi * r *(r + h)






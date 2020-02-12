"""


race = ['john', 'bob', 'tom']
print(race[0])
test = "the christmas tree is green"
test1 = test.split(' ')
print(test1)
print(test1[::-1])
to, swieto, drzewo, jest, zielone = test1
print(to, swieto, drzewo, jest, zielone)



for number in range(4):
    suma = (1 + number)/2 * number

print(suma)

for number1 in range(4):
    print(sum(number1))
"""
suma = 0
for liczba in range(4):
    suma += liczba
print(suma)

def sumuj2_do(liczba):
    return sum([liczba for liczba in range(0, liczba + 1)])
print(sumuj2_do(4))

def sumuj_do(liczba):
    return sum({liczba for liczba in range(0, liczba + 1)})
print(sumuj_do(4))

def sumuj_do3(liczba):
    return (liczba + 1)/2 * liczba
print(sumuj_do3(4))

list = range(5)
print(sum(list))
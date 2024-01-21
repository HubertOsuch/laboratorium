import random
from functools import reduce
def sr_geo(cyfry):
    liczby = reduce(lambda x, y: x * y, cyfry)
    return liczby ** (1.0 / len(cyfry))
poczatek = int(input("Podaj początek przedziału: "))
koniec = int(input("Podaj koniec przedziału: "))
krotka = tuple(random.randint(poczatek, koniec) for i in range(10))
srednia = sr_geo(krotka)

print(f"Podany przedział uwtorzył nastepującą krotkę: {krotka}")
print(f"Średnia geometryczna krotki wynosi: {srednia} ")
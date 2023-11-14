print("Grupa laboratoryjna nr 2")
n = int(input("Podaj ilość studnetów: "))

suma_punktow = 0

s = 1

while s <= n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {s} :  "))

    suma_punktow += punkty

    s += 1

srednia = suma_punktow / n
print(f"Średnia liczba punktów w grupie wynosi: {srednia} ")
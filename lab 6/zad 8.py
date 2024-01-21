import math

def pole_tr(a, b, kat):
    # Sprawdzanie, czy trójkąt jest ostrokątny
    if kat >= 90 or kat <= 0:
        print("Podany kąt nie jest kątem ostrym. Spróbuj ponownie.")
        return None

    # Zamiana kąta na radiany
    kat_st = math.radians(kat)

    # Sprawdzanie, czy trójkąt istnieje
    if a + b <= max(a, b) or a + max(a, b) <= b or b + max(a, b) <= a:
        print("Błędne wymiary boków. Nie można utworzyć trójkąta. Spróbuj ponownie")
        return None

    # Obliczanie pola trójkąta ostrokątnego
    pole = 0.5 * a * b * math.sin(kat_st)
    return pole

# Przykład użycia funkcji
a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
kat = float(input("Podaj kąt trojkąta w stopniach: "))

pole = pole_tr(a, b , kat)

if pole is not None:
    print(f"Pole trójkąta ostrokątnego wynosi: {pole}")
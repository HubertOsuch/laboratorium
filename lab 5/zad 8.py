def potega():
    a = float(input("Podaj podstawe potęgi: "))
    n = int(input("Podaj wykładnik potęgi (liczba całkowita): "))

    wynik = obliczenia(a, n)
    return f"Wynik potęgi {a} do {n} = {wynik}"

def obliczenia(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / obliczenia(a, -n)
    else:
        return a * obliczenia(a, n - 1)
print(potega())

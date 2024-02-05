n = int(input("Podaj liczbę większą od zera: "))
if n > 0:
    suma = 0
    for i in range(1,n+1):
        suma += i

    wynik = suma / n
    print(wynik)
else:
    print("Liczba musi byc większa od zera")
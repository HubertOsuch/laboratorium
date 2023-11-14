liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

start = min(liczba1, liczba2)
koniec = max(liczba1, liczba2)

print(f"Kolejne liczby od {start} do {koniec} to: ")
for x in range(start, koniec +1):
    if x % 2 != 0 :
        continue
    print(x)
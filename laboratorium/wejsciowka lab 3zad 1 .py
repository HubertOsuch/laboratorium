a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

start = min(a, b)
koniec = max(a, b)

print(f"Kolejne liczby parzyste z przedziału od {start} do {koniec} to: ")
for x in range (start, koniec +1 ):
    if x % 2 == 0:
        print(x)
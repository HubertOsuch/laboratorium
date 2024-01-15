import time
odliczanie = int(input("Podaj czas w sekundach: "))
while odliczanie > 0:
    print(f"Do końca odliczania pozostało: {odliczanie} sekund")
    time.sleep(1)
    odliczanie -= 1
print("Koniec odliczania")

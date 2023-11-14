wysokosc_choinki = int(input("Podaj wysokość pierwszej choinki: "))
print("\nPierwsza choinka")
for i in range(wysokosc_choinki):
    print("* " * (i + 1 ))

print("\nDruga choinka")
for i in range(wysokosc_choinki):
    for a in range(wysokosc_choinki - i):
        print(" ",end="")

    for b in range(2 * i - 1):
        print("*",end="")

    print()



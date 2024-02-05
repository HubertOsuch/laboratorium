a=int(input("Podaj początkowy przedział liczb: "))
b=int(input("Podaj końcowy przedział liczb: "))
if a<b:
    suma = 0
    for i in range(a,b+1):
        suma += i
    print(f"Suma liczb od {a} do {b} to {suma} ")
else:
    print("Liczba początkowa musi byc mniejsza od liczby końcowej")

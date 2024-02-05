a=int(input("Podaj początkowy przedział liczb: "))
b=int(input("Podaj końcowy przedział liczb: "))
if a<b:
    for i in range(a,b+1):
        if i % 3==0:
            print(i)
else:
    print("Liczba początkowa musi być większa od końcowej")
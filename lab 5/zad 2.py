def poleT():
    a = float(input("Podaj długość pierwszej podstawy: "))
    b = float(input("Podaj długość drugiej podstawy: "))
    h = float(input("Podaj wysokość trapezu: "))
    pole = (a+b)*h/2
    return pole
print(f"Pole trapezu wynosi: {poleT()}")

print("prostokąt")
dlugosc = float(input("Podaj długość boku prostokąta: "))
szerokosc = float(input("Podaj szerokość boku prostokąta: "))
if dlugosc and szerokosc < 0:
    print("Wprowadzono złe dane")
else:
    pole = dlugosc * szerokosc

    obwod = 2 * (dlugosc + szerokosc)

    print("Pole prostokąta wynosi: ", pole, "cm^2")
    print("Obwód prostokąta wynosi: ", obwod, "cm")
import random
def gra():
    print("Witaj w grze, twoim zadaniem jest odgadnięcie losowej liczby. Pamietaj masz tylko 3 próby na jej odgadnięcie. Powodzenia!")
    try:
        poczatek = int(input("Podaj początek losowania: "))
        koniec = int(input("Podaj koniec losowania: "))
    except ValueError:
        print("Podano niepoprawny zakres losowania. Spróbuj jeszcze raz.")
        return
    if poczatek >= koniec:
        print("Podano niepoprawny zakres losowania. Spróbuj jeszcze raz.")
        return
    elif (poczatek + 9 > koniec):
        print("Niezła próba, ale przedział musi zawierać co najmniej 10 liczb")
        return
    losowa_liczba = random.randint(poczatek, koniec)
    print(f"Spróbuj zgadnąć liczbę z przediału od {poczatek} do {koniec}")
    for proba in range(3):
        try:
            liczba = int(input("Podaj liczbę: "))
            if liczba < poczatek or liczba > koniec:
                print("Podano liczbę spoza zakresu. Spróbuj ponownie")
                continue
        except ValueError:
            print("Podano niepoprawną liczbę. Spróbuj ponownie")
            continue
        if liczba == losowa_liczba:
            print(f"Gratulacje! Udało ci się odgadnąć ukrytą liczbę, była to {losowa_liczba}")
            return losowa_liczba
        elif liczba > losowa_liczba:
            print("Za dużo")
        else:
            print("Za mało")
    print(f"Niestety nie udało ci się odgadąć naszej ukrtej liczby, którą była {losowa_liczba}. Spróbuj ponownie")

gra()
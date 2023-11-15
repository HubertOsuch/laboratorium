koniec = "Dziękujemy za skorzystanie z naszego programu"

while True:
    try:
        dana = int(input("Podaj liczbę całkowitą: "))
        if dana < 0:
            print(f"Podana liczba jest liczbą ujemną. {koniec}")
            break
        elif dana == 0:
            print(f"To jest liczba {dana}")
        elif dana >= 0:
            print(f"To jest liczba {dana}")
            wybor = (input(f"Czy chcesz wyświetlić pierwiastek kwadratowy z liczby {dana}? (tak/nie) "))

            if wybor == "tak":
                pierwiastek = dana ** 0.5
                print(f"Pierwiastkiem kwadratowym liczby {dana} jest {pierwiastek}")

            else:
                print(koniec)
                break

    except ValueError:
        print("Nieprawidłowe dane. Wprowadź liczbę całkowitą")
        break
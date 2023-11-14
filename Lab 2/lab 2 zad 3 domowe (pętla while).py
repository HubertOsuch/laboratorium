while True:
    liczba = int(input("Podaj liczbę całkowitą nie ujemną: "))

    if liczba < 0:
        print("Podano liczbę ujemną. Koniec pętli")
        break
    else:
        print(f"Podano liczbę {liczba}")


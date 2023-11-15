while True:
    try:
        n = int(input("Podaj liczbe narutalną dodatnią z której chcesz obliczyć silnie: "))
        x = 1
        for i in range(1, n + 1):
            x = x * i
        if n <= 0:
            print("Musisz podać liczbę dodatnią. Spróbuj ponownie")

        else:
            print( f"Silnia z liczby {i} to: {x} ")
        break
    except ValueError:
        print("Musisz podać liczbę naturalną. Spróbuj ponownie ")

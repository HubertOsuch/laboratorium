def fibonacci(n):
    if n < 0:
        return "Niewłaściwa liczba, wyraz musi być liczbą naturalną większą od zera."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Przykład użycia:
n = int(input("Podaj n-ty wyraz ciągu Fibonacciego który chcesz poznać: "))
wynik = fibonacci(n)
print(f"{n} wyraz ciągu Fibonacciego to: {wynik}")






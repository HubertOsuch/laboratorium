print("Kalkulator")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

dzialanie = input("Wybierz działanie jakie chcesz wykonać: ")
if dzialanie == "1":
    wynik = a+b
elif dzialanie == "2":
    wynik = a-b
elif dzialanie == "3":
    wynik = a*b
elif dzialanie == "4":
    wynik = a/b
else:
    wynik = a**b

print(wynik)



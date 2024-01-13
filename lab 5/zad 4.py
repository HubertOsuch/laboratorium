def dodatnia():
    x = float(input("Podaj liczbę: "))
    if x > 0:
        return "Liczba jest dodatnia."
    elif x == 0:
        return "Liczba jest równa zero."
    else:
        return "Liczba jest ujemna."
    return x
print(dodatnia())








def poleK():
    r = float(input("Podaj promień koła: "))
    if r > 0:
        pole = 3.14*r**2
        return f"Pole koła wynosi: {pole} "

    else:
        return "Promień musi być dodtani. Spróbuj jeszcze raz"
print(poleK())


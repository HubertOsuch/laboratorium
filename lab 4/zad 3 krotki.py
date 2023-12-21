rachunek_za_prad = {
    "Maj" : 82,
    "Czerwiec" : 75,
    "Liepiec" : 70,
    "Sierpień" : 62,
    "Wrzesień" : 68,
    "Październik" : 79,
    "Listopad" : 85
}
lista_rachunku = list(rachunek_za_prad.values())
#a
maks = max(lista_rachunku)
minimalna = min(lista_rachunku)
suma = sum(lista_rachunku)
srednia = suma / len(lista_rachunku)
print("Maksymalny miesiąc wyniósł: ",maks)
print("Minimalny miesiąc wyniósł: ",minimalna)
print("Suma rachunków za prąd wyniosła: ",suma)
print("Średnia wartość rachunków za prąd wyniosła: ",srednia)
#b
ostatni_miesiac = list(rachunek_za_prad.keys())[-1]
wartosc = rachunek_za_prad[ostatni_miesiac]
print(f"{ostatni_miesiac} to ostatni miesiąc: ", wartosc)
print("Średnia za wszytskie misiące: ",srednia)
if wartosc > srednia:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")
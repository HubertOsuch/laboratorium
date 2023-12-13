imie = (input("Podaj imie: "))
print(f"Witaj {imie}")
wiek = int(input("Podaj swój wiek: "))
print(f"Twoj wiek to {wiek}")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + nazwisko[0].upper()
print(f"Twoje inicjały to {inicjaly}")
#d
lancuch = input("Wpisz co chcesz: ")
for i in range(5):
    print(lancuch)
#e
lancuchdwa = input("Znowu masz dowolność napisz co chcesz: ")
lancuchtrzy = lancuch + " " + lancuchdwa
print(lancuchtrzy)
#f
polowapierwszego = len(lancuch) //2
polowadrugiego = len(lancuchdwa) //2
lancuchpoloczony = lancuch[ :polowapierwszego] + " " + lancuchdwa[polowadrugiego: ]
print(lancuchpoloczony)


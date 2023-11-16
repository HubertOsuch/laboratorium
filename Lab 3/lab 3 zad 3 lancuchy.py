
def imie_nazwisko():

    imie = input("Podaj imię: ")
    print(f"Witaj! {imie}")
    wiek = int(input("Podaj wiek: "))
    print(f"Twój wiek to: {wiek}")
    nazwisko = input("Podaj nazwisko: ")
    inicjaly = imie[0].upper() + nazwisko[0].upper()
    print(f"Twoje inicjały to: {inicjaly}")

def lancuchy():

    lancuch = input("Podaj łańcuch: ")
    for i in range(5):
        print(lancuch)

def lancuch_dwa():
    pierwszy = input("Podaj pierwszy łańcuh: ")
    drugi = input("Podaj drugi łańcuch: ")
    razem = pierwszy + " " + drugi
    print(f"Połączone łańcuchy dają: {razem}")

def lanuch_trzy():
    pierwszy = input("Podaj pierwszy łańcuh: ")
    drugi = input("Podaj drugi łańcuch: ")
    s_pierwszego = len(pierwszy) // 2
    s_drugiego = len(drugi) // 2

    razem  = pierwszy[ : s_pierwszego] + " " + drugi[s_drugiego : ]
    print(f"Połowa pierwszego łańcuha i drugiego to: {razem} ")




print("Program 1 wypisuje imie, nazwisko, wiek i podaje inicjały")
print("Program 2 wpisuje łańcuh i podaje go 5 razy")
print("Program 3 wypisuje dwa łańcuhy i łączy je razem")
print("Program 4 wypisuje dwa łańcuhy i podaje  pierwszą połowę pierwszego i  drugą połowę drugiego")
wybor = input("Wybierz program (1, 2, 3 lub 4): ")
if wybor == "1":
    imie_nazwisko()
elif wybor == "2":
    lancuchy()
elif wybor == "3":
    lancuch_dwa()
elif wybor == "4":
    lanuch_trzy()
else:
    print("Zły wybór")



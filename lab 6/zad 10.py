import datetime
def czas(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    dzien_roku = data.timetuple().tm_yday
    numer_tygodnia = data.isocalendar()[1]
    przed = data - datetime.timedelta(days=14)
    po = data + datetime.timedelta(days=14)
    niedziela = (6 - data.weekday()) % 7
    data_niedziela = data + datetime.timedelta(days= niedziela)
    czas_unixowy = int((datetime.datetime(rok ,miesiac, dzien) - datetime.datetime(1970 , 1, 1 )).total_seconds())
    print(f"a) Dzień roku: {dzien_roku}")
    print(f"b) Numer tygodnia: {numer_tygodnia}")
    print(f"c) Daty na 2 tygodnie przed i po: {przed} - {po}")
    print(f"d) Datę najbliższej niedzieli: {data_niedziela}")
    print(f"e) Czas unixowy bieżącej godziny w podanym dniu: {czas_unixowy}")

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

czas(rok, miesiac, dzien)
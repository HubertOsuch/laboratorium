from datetime import datetime
data_laboratoria = datetime(2023, 12, 19)
data_kolokwium = datetime(2024, 2, 12)
roznica_lab = datetime.now() - data_laboratoria
roznica_kol = data_kolokwium - datetime.now()
print(f"Od ostatnich laboratoriów do obecnych minęło: {roznica_lab}")
print(f"Do kolokwium zostało jeszcze: {roznica_kol}")
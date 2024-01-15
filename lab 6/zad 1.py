#a
import random
numerki = random.randint(1,100)
print(f"Twój szczęśliwy numerek to: {numerki}")
#b
roczniki = [2003, 2004, 2005, 1999, 2002, 2001, 1991]
szczęśliwy_rocznik = random.choice(roczniki)
print(f"Szczęśliwym rocznkiem zostaje rok: {szczęśliwy_rocznik}")
#c
liczby = list(range(1,50))
print("Zwycięskie numerki w losowaniu totolotka to: ",random.sample(liczby, 6))

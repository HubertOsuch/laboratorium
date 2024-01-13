def BMI():
    wzorst = float(input("Podaj swój wzorst w metrach: "))
    waga = float(input("Podaj swoją wage w kilogramach: "))
    wskaznik = waga/(wzorst**2)
    if wskaznik < 18.5:
        return f"Twój wskaźnik BMI jest równy: {wskaznik} oznacza to niedowagę"
    elif 18.5 <= wskaznik < 24.5:
        return f"Twój wskaźnik BMI jest równy: {wskaznik} masz prawidłową wagę"
    elif 25 <= wskaznik < 30:
        return f"Twój wskaźnik BMI jest równy: {wskaznik} oznacza to nadwagę"
    else:
        return f"Twój wskaźnik BMI jest równy: {wskaznik} oznacza to otyłość"

print(BMI())
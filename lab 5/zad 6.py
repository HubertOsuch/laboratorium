def pT():
    a = float(input("Podaj długośc pierwszego boku: "))
    b = float(input("Podaj długośc drugiego boku: "))
    c = float(input("Podaj długośc trzeciego boku: "))
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        polowa = (a+b+c)/2
        pole = (polowa*(polowa-a)*(polowa-b)*(polowa-c))**0.5
        return f"Pole trójkąta wynosi: {pole}"
    else:
        return "Błędne wymiary boków. Nie można utworzyć trójkąta. Spróbuj ponownie"
print(pT())
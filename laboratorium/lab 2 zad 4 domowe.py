x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

najmniejsza = x

if y < najmniejsza:
    najmniejsza = y

if z < najmniejsza:
    najmniejsza = z

najwieksza = x

if y > najwieksza:
    najwieksza = y
if z > najwieksza:
    najwieksza = z

srodkowa = x + y + z - najmniejsza - najwieksza
print("Liczby w kolejności rosnącej", najmniejsza, srodkowa, najwieksza)
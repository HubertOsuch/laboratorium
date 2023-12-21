import random
a = random.randint(3, 7)
b = random.randint(3, 7)
X = {random.randint( 0, 10) for i in range(a)}
Y = {random.randint( 0, 10) for i in range(b)}
print("Zbiór X: ",X)
print("Zbiór Y: ",Y)
#a
liczba_piec = 5 in X
if  liczba_piec:
    print("Zbiór X zawiera liczbe 5")
else:
    print("Zbiór X nie zawiera liczby 5")
#b
podzbior_x = X.issubset(Y)
if podzbior_x:
    print("Zbiór X jest podzbiorem zbioru Y")
else:
    print("Zbiór X nie jest podzbiorem zbioru Y")
#c
podzbior_y = Y.issubset(X)
if podzbior_y:
    print("Zbiór Y jest podzbiorem zbioru X")
else:
    print("Zbiór Y nie jest podzbiorem zbioru X")
#d
nadzbior_x = X.issuperset(Y)
if nadzbior_x:
    print("Zbiór X jest nadzbiorem zbioru Y")
else:
    print("Zbiór X nie jest nadzbiorem zbioru Y")
#e
nadzbior_y = Y.issuperset(X)
if nadzbior_y:
    print("Zbiór Y jest nadzbiorem zbioru X")
else:
    print("Zbiór Y nie jest nadzbiorem zbioru X")
#f
suma_zbiorow = X.union(Y)
print("Suma zbiorów X i Y to: ", suma_zbiorow)
#g
roznica_x_od_y = X.difference(Y)
print("Różnica zbiorów X od Y to: ", roznica_x_od_y)
#h
roznica_y_od_x = Y.difference(X)
print("Różnica zbiorów Y od X to: ", roznica_y_od_x)
#i
iloczyn_zbiorow = X.intersection(Y)
print("Iloczyn zbiorów wynosi: ",iloczyn_zbiorow)
#j
roznica_symetryczna = X.symmetric_difference(Y)
print("Różnica symetryczna zbiorów wynosi: ",roznica_symetryczna)
#k
maks_x = max(X)
maks_y = max(Y)
print(f"Największa wartość zbioru X to: {maks_x}. Największa wartośc zbioru Y to: {maks_y}")
#l
pierwszy = X.pop()
Y.add(pierwszy)
print("Zbiór X po usunięciu pierwszego elementu", X)
print("Zbiór Y po dodaniu pierwszego elementu ze zbioru X", Y)
#m
Y.update(X)
print("Zbiór Y po kopii",Y)
#n
X.clear()
Y.clear()
print("Wyczyszczone zbiory", X, Y)
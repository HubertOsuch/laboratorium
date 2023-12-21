listaimion = ["Ala", "Tomek", "Piotrek", "Hania"]

print(listaimion)
#a
posortowana= sorted(listaimion)
print(posortowana)
#b
listaimion.append("Zuzia")
listaimion.append("Bartek")
print(listaimion)
ostatnia_osoba = listaimion.pop()
print(ostatnia_osoba)
#c
listaimion.insert(2, "Karol")
print(listaimion)
#d
listaimion.reverse()
zdublowana_lista = listaimion * 2
print(zdublowana_lista)
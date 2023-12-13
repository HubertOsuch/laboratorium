listazakupow = {"papryka":6.99, "ryż":9.99, "piwo":3}
print(listazakupow)
suma = 0
for key in listazakupow:
    suma += listazakupow[key]
    print(key)

print(suma)
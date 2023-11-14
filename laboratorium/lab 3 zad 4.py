n = int(input("Ile wyrazów ciągu obliczyć: "))
a = int(input("Podaj pierwszy wyraz ciągu arytmetycznego: "))
r = int(input("Podaj różnice ciągu arytmetycznego: "))
for i in range(n):
    x = a + i * r
    print(x)
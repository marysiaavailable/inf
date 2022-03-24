import random
print("podaj zakres liczb z ktorych wylosujemy szesc liczb")
a=int(input("Podaj wartosc minimalna:"))
b=int(input("Podaj wartosc maksymalna:"))
random.randint(a,b)
for i in range(6):
    print(random.randint(a,b))



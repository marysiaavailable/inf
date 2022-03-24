print("Podaj trzy dlugosci bokow w trojkacie")
a=int(input("podaj wartosc a:"))
b=int(input("podaj wartosc b:"))
c=int(input("podaj wartosc c:"))
if a+b<=c:
    print(" nie mozna")
elif b+c<=a:
    print("nie mozna")
elif c+a<=b:
    print(" nie mozna")
else:
    print("mozna")

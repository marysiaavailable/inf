import math
a=int(input("Podaj wartosc a:"))
b=int(input("Podaj wartosc b:"))

print("dodawanie", a+b)
print("odejmowanie",a-b)
print("odejmowanie",b-a)
print("mnozenie", a*b)
if b==0:
    print("nie mozna dzilic przez 0")
else:
    print("dzielenie",a/b)
if a==0:
    print("nie mozna dzilic przez 0")
else:
    print("dzielenie",b/a)
print(a,"do potegi", b,"wynosi", a**b )
print(b,"do potegi", a,"wynosi", b**a )
print(math.hypot(a,b))
import math
a=int(input("Podaj swoja wage w kg:"))
b=float(input("Podaj swoj wzrostu w m:"))
c=b**2
bmi=a/c
print("twoje bmi wynosi", bmi)

if bmi<20:
    print("Niedowaga")
elif 20<=bmi<25:
    print("Prawidłowa waga")
elif 25<=bmi<=30:
    print("Nadwaga")
elif bmi>30:
    print("Otyłość")
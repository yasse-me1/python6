#1
a=int(input("a sonni kiriting: "))
b=int(input("b sonni kiriting: "))


if(a > b):
    print("a katta b dan")
elif(a == b):
    print('teng')
else:
    print('b katta a dan')
#2
age=int(input("Yoshingizni kiriting: "))
if age>=18:
    print("Balog'at yoshiga yetgansiz")
else:
    print("Balog'at yoshiga yetmagansiz")
#3
son1=int(input("Sonni kiriting: "))
son2=int(input("2-sonni kiriting"))
if(0<son1 and 0<son2):
    print(True)
else:
    print(False)
#4
ism=(input("Ismingizni kiriting: "))
yosh=(input("yoshingizni kiriting: "))
if ism=="Ali" and yosh=="18":
    print("Hush kelibsiz Ali")
#5
son1=int(input("1-sonni kiriting: "))
son2=int(input("2-sonni kiriting: "))
son3=int(input("3-sonni kiriting: "))
javob=(son1+son2+son3)
print(javob/3)

    


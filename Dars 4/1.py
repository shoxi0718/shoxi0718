import os
os.system("cls")
#!!Funksiya def
def salom_ber():
    print("Assalomaleykum")
def Xayrlash():
    print("Salomat bo'ling")
salom_ber()
Xayrlash()
def qosh(a,b):
    y = a+b 
    print(y)
# def sum(n:float, c:int):
#!!!!!!!Kattasini chiqaruvchi1-usul.
def Katta_chiqar(a,b,c,d,e):
    s=max(a,b,c,d,e,)
    print(s)
print("Eng katta son : " , end= "")
Katta_chiqar(2,3,4,5,6)
#!!!!!!!Kattasini chiqaruvchi 2-usul.
def Katta_chiqar(a,b,c,d,e):
    return max(a,b,c,d,e,)
a,b,c,d,e =map(int, input().split())
k = Katta_chiqar(a,b,c,d,e)
print("Eng katta son :", k)
#!Daraja 1-usul
def Daraja(a,b,c):
    return"""
{} darajasi{},
{} darajasi{},
{} darajasi{}
""".format(a, a**a, b, b**b, c, c**c)
a,b,c = map(int,input("N: ").split())
c  = Daraja(a,b,c)
print(c, type(c))
#!Daraja 2-usul
def Daraja(a,b,c):
    return print("""
{} darajasi{},
{} darajasi{},
{} darajasi{}
""".format(a, a**a, b, b**b, c, c**c))
a,b,c = map(int,input("N: ").split())
Daraja(a,b,c)
#Tubini qaytaruvchi dastur 1-usul 
def  Tublikka_tekshir():
    lst = [ 24,6,2,5,]
    s = 0 
    for i in range(len(lst)):
        if(lst[i] % 2 !=0 ):
            s += 1
    if(s > 0):
        print("Tub son bor")
    else:
        print("Tub son yuq ")
#Tubini qaytaruvchi dastur 2-usul
#!Mahsulot


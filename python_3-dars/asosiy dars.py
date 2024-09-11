import os  
os.system("cls") 
#list ichidagi eng katta qismini topish
l1 =[int(input())for i in range(int(input("N1 ")))]
l2 =[int(input())for i in range(int(input("N2 ")))]
l3 =[int(input())for i in range(int(input("N3 ")))]
l4 =[int(input())for i in range(int(input("N4 ")))]
l = [l1,l2,l3,l4]
print(l); katta = 0 
for i in l :
    if sum(i) > katta:
#sum() bu yerda shunchaki funksiya sum degan o'zgaruvchi ochmadik
#python dasturlash tilidahgi uzida hisoblab ketuvchi funksiya 
        katta = sum(i)
#2-usul.
for j in l:
    if (sum(j) == katta):
        print(j)
#ichiga soz qushish , ls[i]ga elemnt qushib quyadi.
ls = list(map(int, input().split()))
soz = input("So'zni kiriting: ")
x = []
for num in ls:
    if num > 0:
        x.append(soz + str(num))
print(x)
#!key va value kiritish .
dic = dict()
for i in range( int(input("N : "))):
    k = int(input("Key "))
    dic[k] = input("Velyu ")
print(dic)
# list() va tuple() farqi shundaki listda mlumotlarni o'chirish , qo'shish ,
#  ayirish indeksi buyicha sort()lash mumkin 
#Lekin tuple()leda bunday amallar mavjud emas . 
# tuple()da br xil elementlarni saqlab bulmaydi unda indeks ham mavjud emas.
#Tupleda berilhgan qiymatlarni uzgartirish uchun uni listga utkazish kerak 

import os  
os.system("cls")
#Juft sonlarni chiqarish
n  = int(input("Sonni kiriting :"))
for i in range (1 , n +1):
  if i % 2==0 :
    print(i , end = " ")
#Raqamlarini alohida chiqarish .
son = int (input ("Sonni kiriting"))
while son :
  print(son %10, end = " ")
  son//= 10 
# 1 dan N gacha orasidan 3 ga 5 ga 7 ga bulinadiganini chiqarish 
n = int(input("N ni kiriting :"))
for i in range (1 , n , 1):
    if(i %3 ==0 and i % 5  ==0 and i % 7 ==0 and i % 2 ==0 ):
        print(i, end = " ")
#1 dan n gacha 3 va 8 ga bulinuvchi 
n = int(input("N ni kiriting :"))
yig = 0 
for i in range (1 , n , 1):
    if(i % 3 ==0 and i % 8  ==0 and i % 2 ==0 ):
        yig+=i
print("Yigindisi " , yig )
#40 dan 80 gacha bolgan sonlar ichida 7 ga bulinadigan juftlar ichida
# 6 va 4 ga bulinuvchilarini tekhirish  
n = 180 
yig = 0 
for i in range (40 , n , 1):
    if(i % 7 ==0 and i % 2 ==0 ):
        if(i % 6 ==0 and i % 4 ==0 ):
          yig+=i
print("Yigindisi " , yig )
#A harfi bulsa a harfini olib tashlash
s = " salom "
for i in s:
   if(i == 'a'):
      continue
   print(i , end = "")
#sozdi uzunligini chiqarish 
soz = "Salom Bolalar"
for i in range(len(soz)):
   print(soz[i])
#raqam urniga A ni quyebdi 1chi usul
soz = input("Matinni kiriting ")
soni = 0  
for i in soz:
    if (i.isdigit()):
        i ='A'
    print(i, end = "")
#raqam urniga A ni quyebdi 2chi usul
soz = input("Matinni kiriting ")
soni = 0  
for i in range(len(soz)):
    if not (soz[i].isdigit()):
        print(soz[i], end = "")
    else:
        print("A", end="")
#!! Kattani kichikka kichikni kattaga son belgi
 #bulsa tashlab ketadi probel orniga  ' ' quyuvchi dastur 
soz = input("Gap kiriting : ")
text = ""
for i in range(len(soz)):
    if(soz[i].islower()):
        text += soz[i].upper()
    elif(soz[i].isupper()):
        text += soz[i].lower()
    elif(soz[i].isspace()):
        text += ' '
    else :
        continue
print(text)
# ! teng tomonli uch burchak 
n = int (input("N "))
for i in range(1,  n +  1) :
    for j in range( n - i ) :
        print(" ", end="")
    for k in range (1, i + 1):
        print("* ", end="")   
    print()























import os
os.system("cls")
a, b, c  = map(int, input("Sonlarni kiriting  ").split())
soni = 0 ;  
if (a % 2 ==0):
    soni += a
if (b % 2 ==0):
    soni += b
if (c % 2 ==0):
    soni += c
print("Juft sonlar yigindisi : ", soni)







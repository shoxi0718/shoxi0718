import os
os.system("cls")
a, b, c, d, e, f  = map(int, input("SOnlarni kiriting  ").split())
soni = 0 ; soni1 = 0 
if (a % 2 ==0):
    soni += 1
else :
    soni1 += 1
if (b % 2 ==0):
    soni += 1
else :
    soni1 += 1
if (c % 2 ==0):
    soni += 1
else :
    soni1 += 1
if (d % 2 ==0):
    soni += 1
else :
    soni1 += 1
if (e % 2 ==0):
    soni += 1
else :
    soni1 += 1
if (f % 2 ==0):
    soni += 1
else :
    soni1 += 1
print("Juft sonlar yigindisi : ", soni)
print("Toq  sonlar yigindisi : ", soni1)







import os
os.system("cls") 
n = input(" Sonni kiriting: ")
x =""
yig = 0
for i in n:
    raqam = int(i)
    if raqam % 2 !=0 :
        x += i 
        yig+=raqam
print(*x, sep=" + ", end=" = ")
print(yig)

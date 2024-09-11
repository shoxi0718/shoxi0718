import os
os.system("cls") 
n = input(" Sonni kiriting: ")
katta = 0
for char in n:
    raqam = int(char)
    if raqam > katta:
        katta = raqam
print(katta)

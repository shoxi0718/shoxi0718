import os
os.system("cls")
matn = input("Marhamat matnni kiriting: ")
soz = ""
for i in matn:
    if i == ' ':
        break
    soz += i
print("Birinchi so'z:", soz)

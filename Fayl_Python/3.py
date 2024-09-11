import os
import string
os.system("cls")  
with open("Lotin_harf_top.txt", "r") as file:
    oqibol = file.read()
harflar = set(string.ascii_letters) 
sum = 0
for i in oqibol:
    if i in harflar:
        sum += 1
print(f"Faylda {sum} ta Lotin harfi mavjud.")

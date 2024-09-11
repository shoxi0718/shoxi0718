import os
os.system("cls")
with open("matn.txt", "r") as file:
    matn = file.read()
raqamlar = sum(c.isdigit() for c in matn)
print(f"{raqamlar}ta raqam mavjud.")

import os
os.system("cls")
with open("Tartibla1.txt", "r") as file:
    matn = file.read().strip()
harflar = [i for i in matn if i.isalpha()]
harf_sorted = sorted(harflar)
with open("sorted1_asc.txt", "w") as file:
    file.write(" ".join(harf_sorted))
print("Raqamlar o'sish tartibida 'sorted1_asc.txt' faylga yozildi.")

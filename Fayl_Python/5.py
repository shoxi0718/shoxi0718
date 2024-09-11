import os
os.system("cls")
with open("Tartibla.txt", "r") as file:
    matn = file.read().strip()
raqamlar = [i for i in matn if i.isdigit()]
raqamlar_sorted = sorted(raqamlar, key=int)
with open("sorted_asc.txt", "w") as file:
    file.write(" ".join(raqamlar_sorted))
print("Raqamlar o'sish tartibida 'sorted_asc.txt' faylga yozildi.")
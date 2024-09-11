import os
os.system("cls") 
with open("Takrorla.txt", "r") as file:
    oqibol = file.read()
gap = oqibol.split()
if gap:
    soz = gap[0]
    print(f"{soz} {soz}")
else:
    print("Faylda hech qanday so'z topilmadi.")

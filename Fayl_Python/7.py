import os
import re
os.system("cls")  
with open("input.txt", "r") as file:
    matn = file.read().strip()
raqamlar = re.findall(r'\d+', matn)
raqamlar_saqla = '+'.join(raqamlar)
print(raqamlar_saqla)

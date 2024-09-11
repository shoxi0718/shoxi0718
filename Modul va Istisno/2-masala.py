
import os
os.system("cls")


def Bin_Faylqil(n):
    if n == 0:
        return "0"
    binfayl = ""
    while n > 0:
        binfayl = str(n % 2) + binfayl
        n = n // 2
    return binfayl
n = int(input("Marhamat sonni kiriting  :"))
print(Bin_Faylqil(n))  

import os
os.system("cls") 
n = input("Sonni kiriting: ")
boshi = int(n[0])
oxri = int(n[-1])
if boshi > oxri:
    print(boshi)
else:
    print(oxri)

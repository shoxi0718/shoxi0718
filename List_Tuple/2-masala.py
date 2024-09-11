import os
os.system("cls") 
gap = input("Gap kiriting: ")
soz = gap.split()
n = []
for i in soz:
    n.append(i.lower())
x = []
while n:
    kichik = n[0]
    for i in n:
        if i < kichik:
            kichik = i
    x.append(kichik)
    n.remove(kichik)
print(" ".join(x))

import os
os.system("cls")
n = int(input("n ni kiriting: "))
yig = 0
son = []
qoshiluvchi = 0
for i in range(n):
    qoshiluvchi = qoshiluvchi * 10 + 2
    son.append(str(qoshiluvchi))
    yig += qoshiluvchi
natija = '+'.join(son)
print(f"{natija}={yig}")

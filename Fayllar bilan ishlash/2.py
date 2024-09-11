import os 
os.system("cls")
f = open("soz.txt", "r")
res , ls = [], []
data = f.read()
for i in data.split("\n"):
    ls.extend(i.split())
for l in ls:
    res.extend(l.split())
natija = sorted (res, key = len )
for i in natija:
    print(f"{i}==>{len(i)}") 
print("Max  - ", natija[-1])
print("Min  - ", natija[0])


import os 
import sys
os.system("cls")
serya = """Muhammadrasul doskaga qarang .
Farruxbek o'ynamang.  
Muhriddin to'g'ri o'tring ."""
file = open("soz.txt", "w")
file.write(serya)

# lis = [ "Kimdir\n","Nimadir\n","Qachondir\n",]
# file.writelines(lis)
# file.close()
lis = [ "Kimdir","Nimadir","Qachondir",]
file.writelines(lis)
for i in lis:
    file.write(i)
    file.write(" ") 
file.close()
#! Fayldan o'qish .
f = open("soz.txt", "r")
matn = f.read()
print(matn, end="\n\n")
f.seek(0)
for i in f:
    for j in i :
        print(j, end="")
f.seek(0)
print()
text = f.readline()
print(text)
f.seek(0)
print ()
print()
ls = f.readlines()
print(ls)
for i in ls:
    for j in i : 
        print(j, end=" * ")
f.close()
#!Faylga Ma'lumot qo'shish . 
 
f = open("soz.txt", "r")
if(f.readable()):
    print("Fayldan ma'lumot o'qishingiz mumkin 😊")
else:
    sys.exit("Sizga ma'lumotlarni o'qishga ruxsat yuq🤕")
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


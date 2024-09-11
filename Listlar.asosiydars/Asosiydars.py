import os 
os.system("cls")
#1.Kiritish Chiqarish
lst1 = []
ls = list()
print(type(lst1))
print(type(ls))
lst1 =[12, 34, 45,667,34]
print(*lst1)
print(lst1[3])
for i in lst1:
    print(i)
print("\n")
for i in range(len(lst1)):
    print(lst1[i])
#2.List ichida append()
for i in range(len(lst1)):
    if(type(lst1[i]) ==str or type(lst1[i]) ==bool):
        print(lst1[i])
# ! \/ ! # 
print(ls)
ls.append(12)
print(len(ls))
n = int(input("N:"))
for i in range(n):
    k =input()
    ls.append(k)
print(ls)
print(len(ls))
#!append
ls = ["salom", 12 , True]
print(ls)
ls.append(13124,34)#
print(ls)
#!insert
ls.insert(0, "mana")
print(ls)
ls.insert(2, False)
print(ls)
#!remove
ls.remove(12)
print(ls)
ls.remove("salom")
print(ls)
#! pop 
ls.pop(2)
print(ls)
d = ls.pop()
print(d)
print(ls)
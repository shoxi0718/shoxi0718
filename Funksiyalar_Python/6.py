import os
os.system("cls")
def Qoshish(lst,lst1):
    yangi = []
    katta = max(len(lst), len(lst1))
    for i in range(katta):
        if i < len(lst):
            yangi.append(lst[i])
        if i < len(lst1):
            yangi.append(lst1[i])
    print("Qo'shilgan listlar jamlanmasi :")
    print(yangi)
a = [1, 2, 3,4,5]
b = [11, 22, 33]
Qoshish(a,b)
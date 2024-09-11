import os
os.system("cls") 
ls = [(1 , 2 , 3)]
for i in range(len(ls)):
    ls[i] = list(ls[i])
    ls[i][-1] = 100
ls = tuple(ls[i])
print(ls)
import os
os.system("cls")
def Kvadrat_Kutaramiz(lst):
    return list(map(lambda x: x**2, lst))# ** cha bu yerda darajaga oshirish
n = [1, 2, 3, 4, 5]
kvadrat = Kvadrat_Kutaramiz(n)
print(kvadrat)

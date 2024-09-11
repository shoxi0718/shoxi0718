import os
os.system("cls")

def Ozgartir(lst):
    tahla = [i for i in lst if i != 0]
    nol = [x for x in lst if x == 0]
    return tahla + nol
lst = [3, 4, 0, 0,  6, 0, 9, 10, 7, 3, 0, 0, 2, 9, 7, 1]
lst1 = Ozgartir(lst)
print("O'zgarmagan holati : ")
print(lst)
print("O'zgarishdan keyingi holati:")
print(lst1)







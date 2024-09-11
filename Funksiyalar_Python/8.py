import os
os.system("cls")
def Sarala(a,b):
   x = set(a)
   y = set(b)
   ab = x-y
   ba = y-x
   c = sorted(list(ab.union(ba)))
   print("Takrorlanmagan elementlar =", c)
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Sarala(lst,lst1)
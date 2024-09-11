import os
os.system("cls")
def Sarala(a,b):
   x = set(a)
   y = set(b)
   c = sorted(x & y)
   print("Yangi list =", c)
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Sarala(lst,lst1)
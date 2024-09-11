import os
os.system("cls")
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst = [tuple(i[:-1] + (100,)) for i in lst]
print(lst)

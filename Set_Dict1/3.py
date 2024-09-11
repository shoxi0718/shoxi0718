import os
os.system("cls")
lst = [[1, 'Jean castor', 'V'], [2, 'Lula powell', 'V'], [3, 'brian howell', 'VI']]
lst = {item[0]: item[1:] for item in lst}
print(lst)

import os
os.system("cls")
lst = [[10], [40, 32,56 ], [ 56, 25], [10, 240], [10], [40]]
lst1 = [tuple(i) for i in lst]
tupldan_setga = set(lst1)
listgaQayt = [list(t) for t in tupldan_setga]
print(listgaQayt)

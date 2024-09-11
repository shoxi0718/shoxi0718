import os
os.system("cls")
lst = [1, 2, 33, 5, 6, 7, 7]
x = int(input("Sonni kiriting: "))  
index = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == x:
            index.append((i, j))
if index:
    for pair in index:
        print(f"{pair[0]} , {pair[1]}")
else:
    print("Hech qanday juftlik topilmadi.")

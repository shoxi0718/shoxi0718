import os
os.system("cls")
n = int(input("N: "))
set = {}
for i in range(n):
    key = input("Key: ")
    value = int(input("Value: "))
    set[key] = value
set1 = sorted(set.items(), key=lambda item: item[1], reverse=True)
print("Eng katta 3 ta qiymatli kalitlar:")
for key, value in set1[:3]:
    print(f" ({key} : {value} ) ", end="")

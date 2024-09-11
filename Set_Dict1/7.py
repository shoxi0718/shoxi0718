import os
os.system("cls")
set = {1: 5 , 2: 10 , 3: 45 ,  4: 8 , 5 : 234}
katta = max(set.values())
kichik = min(set.values())
set1 = [key for key, i in set.items() 
                  if i == katta or i == kichik]
for j in set1:
    del set[j]
print(set)

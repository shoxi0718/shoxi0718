import os
os.system("cls")
son = [61, 228, 9] 
son2 = list(map(str, son))
son2.sort(key=lambda x: x*10, reverse=True)
if son2[0] == '0':
    yig = '0'
else:
    yig = ''.join(son2)
print(f"Eng katta soni {yig}")

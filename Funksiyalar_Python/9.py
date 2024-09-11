import os
os.system("cls")  
def Ochiramiz_Takrorlansa(a):
    x = []
    y = []
    for num in a:
        if num in x:
            y[x.index(num)] += 1
        else:
            x.append(num)
            y.append(1)
    chiqar = []
    for i in range(len(x)):
        if y[i] >= 2:
            if x[i] not in chiqar:
                chiqar.append(x[i])
    chiqar_s = sorted(chiqar)
    print("lst =", chiqar_s)
n = int(input("N : "))  
son = list(map(int, input().split()))
Ochiramiz_Takrorlansa(son)

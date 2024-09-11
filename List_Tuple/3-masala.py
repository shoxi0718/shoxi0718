import os
os.system("cls")  

n = int(input("Sonni kiriting: "))
for i in range(1, n+1):
    yig = 0
    for j in range(1, i+1 ):
        yig += j
        if j > 1:
            print("+", end="")
        print(j, end="")
    print("=" + str(yig))

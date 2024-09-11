import os
os.system("cls")
a, b, c  = map(int, input("SOnlarni kiriting : ").split())
katta = 0 
if ( a==b and b==c ):
    print("3 ta son ham teng ekan !")
elif ( a >= b and a >= c):
    print(f"{a} katta ekan! ")
elif ( b >= a and b >= c):
    print(f"{b} katta ekan! ")
elif ( a==b and b==c ):
    print("3 ta son ham teng ekan !")
else : 
    print(f"{c} katta ekan! ")
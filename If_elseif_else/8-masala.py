import os
os.system("cls")
a, b, c ,d  = map(int, input("SOnlarni kiriting : ").split())
son = 0 
if a % 2 ==0 :
    son +=1 
if b % 2 ==0 :
    son +=1 
if c % 2 ==0 :
    son +=1 
if d % 2 ==0 :
    son +=1 
if son >=2 :
    print(a , b , c , d )
else : 
    print(0)
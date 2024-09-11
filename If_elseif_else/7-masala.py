import os
os.system("cls")
a = int (input ("Sonni kiriting "))
if a % 3 ==0  and a % 5 ==0 :
    print("FIZZBUZZ")
elif a % 3 ==0 :
    print("FIZZ")
elif a % 5 ==0 :
    print("Buzz")


import os
os.system("cls") 
n = 180 
yig = 0 
for i in range (40 , n , 1):
    if(i % 7 ==0 and i % 2 ==0 ):
        if(i % 6 ==0 and i % 4 ==0 ):
          yig+=i
print("Yigindisi " , yig )
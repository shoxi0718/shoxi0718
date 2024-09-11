import os  
os.system("cls") 
matn = input("Matinni kiriting: ")
yig = 0 
for i in matn:
   if(i.isdigit()):
     yig += 1 
print(f"Matnda {yig} ta raqam  bor :" , end= "")
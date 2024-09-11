import os
os.system("cls")
lst = input("Ismlar ro'yxatini kiriting: ").split()
izlash = []
for ism in lst:
    #  tozalash va kichik harfda qilish
    ism = ism.strip().lower()
    if len(ism) > 1 and ism[0] == 'a' and ism[-1] == 'a':
        izlash.append(ism)
        print("bu ism tugri \n",izlash)
    else :
        print("Noto'g'ri kiritish!")

import os
os.system("cls")

def Hisobla(a:int , b :int):
    try:
        natija = a/b
    except ZeroDivisionError:
        print ("Nolga bulib bulmaydi ")
    except TypeError:
        print("Bu str")
    else :
        print(natija)

Hisobla(3,4)


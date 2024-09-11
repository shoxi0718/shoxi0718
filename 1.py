#!!Terminalni tozalash uchun ishlatiluvchi funksiya 
import os
os.system("cls")
# kirish qismi . 
print("Va nihoyat 3 oy utib pythonga keldik")
son = 123 #int()
satr = "bu soz" #string()
b = True #bool()
fson = 123.45 #float()
# !!Berilgan qiymatlarni printda chiqarish.
#"""  """ Bu kop qatorli komment 
print(fson, type(fson))
print(b, type(b))
print(satr, type(satr))
print(son, type(son))
print("salom "  *  2)
son = "Nima"
print(son , type(son))
# !!Textlar  bn ishlash 
text = "Salom bolalar Bugun kun issiqaa"
text = "yaxshimisizlar "
print(text[1:5:1])
print(text[1: :1])
print(text[::1])
print(text[::-1])
print(text[12:1:-1])
print(end= "\n\n")
print(text[::-2])
#!!!Format qilib o'rnini ko'rish 
son = 123; bol = True 
haqiqiyson = 123.23; soz = "salom"
print(f"int son {son}\nBoolQiymat {bol}\nFloat son {haqiqiyson}\nStr qiymat {soz}")
print("int son {}\nBoolQiymat {}\nFloat son {}\nStr qiymat {}".format(son, bol, haqiqiyson, soz))
#!!Taqqoslash amallari 
s = int (input("Son : "))
b = s != 0
print(b)
#!!Sonlarning qiymatini  almashtirish 
print("Sonlarni kiriting ")
a = int (input("A==> "))
b = int (input("B==> "))
a, b = b, a
print(a)
print(b)
#!!!bu usul sal murakkab 
a = 1; b=2; c=3; d=4; e=5; 
yig = a + b +c + d + e 
print(f"{a} + {b} + {c} + {d} + {e} = {yig} " )
#!!Bunisi osoon 
print(1,2,3,4,5, sep-" + ", end=" = ")
print(1+2+3+4+5)
s = input("Matn Kiriting: ")
print(*s, sep="*")
#!!Tortburchak perimetri 
a, b ,  = map(int, input("SOnlarni kiriting  ").split())
P = (a + b)*2
print(("Perimetri "), P)

import os
os.system("cls")
def Yaqinini_Top(char):
    unli = 'aeiou'
    # harfning ASCII kodini olish  ord()
    ozgartr = ord(char)
    unlini_ol = {v: abs(ozgartr - ord(v)) for v in unli}
    yaqn = min(unlini_ol, key=unlini_ol.get)
    return yaqn
n = input("Bitta harf kiriting : ")
print(Yaqinini_Top(n))

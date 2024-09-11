import os
os.system("cls") 
#!!!! 1-usul. faqat nechta unliligimnii tekshiradi . 
# matn = input("Matinni kiriting: ")
# yig = 0
# # Unli harflar ro'yxati
# unli_harflar = 'aeiou'
# for i in matn:
#     if (i.lower() in unli_harflar):
#         yig += 1
# print(f"Matnda {yig} ta unli harf bor.")
matn = input("Matinni kiriting: ")
a = 0 ; e = 0 ; u = 0 ; i = 0 ;o = 0
for harf in matn:
    if harf == 'a':
        a += 1
    elif harf == 'e':
        e += 1
    elif harf == 'u':
        u += 1
    elif harf == 'i':
        i += 1
    elif harf == 'o':
        o += 1
print(f"a harfi: {a} ta")
print(f"e harfi: {e} ta")
print(f"u harfi: {u} ta")
print(f"i harfi: {i} ta")
print(f"o harfi: {o} ta")

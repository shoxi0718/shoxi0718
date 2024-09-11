import os
os.system("cls")
matn = input("Matnni kiriting: ")
# strip() metodi orqali bosh va oxiridagi probelni olib tashlash
gap = [sentence.strip() for sentence in matn.split('.') if sentence]
soz = [word for sentence in gap for word in sentence.split()]
print("So'zlar:", soz)
print("Gaplar:", gap)

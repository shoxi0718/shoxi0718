import os
os.system("cls")
son = input("Sonlarni kiriting : ")
# vergul bilan ajrating bulmasa list holat bulmaydi error beradi
# dastur faqat br xonali sonlar orasida tekshiradi iloji boricha 0 dan 9 gacha kiriting 
sonlar = [int(x) for x in son.split()]
juft_sonlar = [i for i in sonlar if 0 <= i < 10 and i % 2 == 0]
print("1-raqami juft sonlar:", juft_sonlar)

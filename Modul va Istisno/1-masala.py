import os
os.system("cls")
def Sozga_aylantr(n):
    birlar = ["", "bir", "ikki", "uch", "tort", "besh", "olti", "yetti", "sakkiz", "toqqiz"]
    onlar = ["on", "on bir", "on ikki", "on uch", "on tort", "on besh", "on olti", "on yetti", "on sakkiz", "on toqqiz"]
    yuzlar = ["", "on", "yigirma", "ottiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
    minglar = ["", "ming", "ikki ming", "uch ming", "tort ming", "besh ming", "olti ming", "yetti ming", "sakkiz ming", "to'qqiz ming"]
    if n == 0:
        return "nol"
    soz_bilan = []
    if n >= 1000:
        minglar1 = n // 1000
        soz_bilan.append(minglar[minglar1])
        n %= 1000

    if n >= 100:
        yuzlar1 = n // 100
        if yuzlar1 > 0:
            soz_bilan.append(birlar[yuzlar1] + " yuz")
        n %= 100
    if n >= 20:
        yuzlar1 = n // 10
        if yuzlar1 > 0:
            soz_bilan.append(yuzlar[yuzlar1])
        n %= 10
    if n >= 10:
        soz_bilan.append(onlar[n - 10])
    elif n > 0:
        soz_bilan.append(birlar[n])
#strip() metodi satrning boshidan va oxiridan bo‘shliq, tabulyatsiya (tab),
#  yoki yangi qator belgilari kabi belgilardan tozalaydi.
    return " ".join(soz_bilan).strip()
son = int(input("Sonni kiriting (1 dan 10000 gacha): "))
if 1 <= son <= 10000:
    print(Sozga_aylantr(son))
else:
    print("Kiritilgan son 1 dan 10000 gacha bo'lishi kerak.")

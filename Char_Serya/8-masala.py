import os
os.system("cls") 
matn = input("Matn: ").split()
n = 5
if len(matn) >= n:
    #capitalize() birinchi belgi katta, qolganlari esa kichik bo'lgan satrni qaytaradi.
    print(matn[0].capitalize(), end=" ")
    for i in range(1, n):
        print(matn[i], end=" ")
    print(".")
else:
    # ,join() qator ajratuvchi bilan ajratilgan ketma-ketlik elementlarini birlashtirish uchun 
    # ishlatiladigan o'rnatilgan string funktsiyasi. 
    # Bu funksiya ketma-ketlik elementlarini birlashtiradi va uni satrga aylantiradi.
    print(" ".join(word.capitalize() for word in matn), end=" ")
    print(".")
if len(matn) > n:
    text = matn[n:]
    text[0] = text[0].capitalize()
    print(" ".join(text), end=" ")
    print(".")

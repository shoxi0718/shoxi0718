soz = input("So'zni kiriting: ")
harf = input("Almashtirilishi kerak bo'lgan harfni kiriting: ")
if len(harf) != 1:
    print("Iltimos, faqat birta harfni kiriting.")
else:
    katta = ''.join([char.upper() if char == harf else char for char in soz])
    print(katta)

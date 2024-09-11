# Faylni ochamiz
with open('example.txt', 'r') as fayl:
    # Birinchi satrni o‘qiymiz
    birinchi_satr = fayl.readline()
    print("Birinchi satr:", birinchi_satr.strip())  # .strip() qator oxiridagi yangi satr belgisini olib tashlaydi

    # Ikkinchi satrni o‘qiymiz
    ikkinchi_satr = fayl.readline()
    print("Ikkinchi satr:", ikkinchi_satr.strip())

    # Faylning qolgan satrlarini o‘qiymiz
    qolgan_satrlar = fayl.readlines()
    print("Qolgan satrlar:")
    for satr in qolgan_satrlar:
        print(satr.strip())

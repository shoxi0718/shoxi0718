N = 8
sonlar = [1, 2, 6, 4, 3, 2, 4, 6]

# Takrorlanish sonini hisoblash uchun yordamchi ro'yxatlar
unique_elements = []
count_elements = []

# Har bir elementning qanchalik takrorlanganligini hisoblaymiz
for num in sonlar:
    if num in unique_elements:
        count_elements[unique_elements.index(num)] += 1
    else:
        unique_elements.append(num)
        count_elements.append(1)

# Ikki yoki undan ko'p marta takrorlangan elementlarni yig'amiz
result = []
for i in range(len(unique_elements)):
    if count_elements[i] >= 2:
        result.append(unique_elements[i])

# Natijani tartiblaymiz
sorted_result = sorted(result)

print("sonlar =", sorted_result)
import os
os.system("cls") 
matn = input("Matinni kiriting: ")
text = ""
for i in range(len(matn)):
    if matn[i] == 'a' or matn[i] == 'A':
        text += 'b'
    elif matn[i] == 'b' or matn[i] == 'B':
        text += 'a'
    else:
        text += matn[i]  # Boshqa belgilarni o'z holida saqlash

print(text)

text = "salom aziz nima gap"
soz = text.split()
teskari = []
for word in soz:
    if len(word) % 2 == 1: 
        teskari.append(word[::-1])  
    else: 
        teskari.append(word)  

chiqar = ' '.join(teskari)
print(chiqar)

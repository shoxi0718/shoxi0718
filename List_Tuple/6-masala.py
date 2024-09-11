son = 20

tub = []
count = 0
son1 = 20 + 1
while count < 5:
    if son1 > 1:
        tub = True
        for i in range(2, int(son1**0.5) + 1):
            if son1 % i == 0:
                tubmas = False
                break
        if tubmas:
            tub.append(son1)
            count += 1
    son1 += 1
print(" ".join(map(str, tub)))

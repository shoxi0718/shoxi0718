import os
os.system("cls")
def split_even_odd(lst):
    juft = list(filter(lambda x: x % 2 == 0, lst))
    toq = list(filter(lambda x: x % 2 != 0, lst))
    return juft, toq
lst = [13,34,54,23,43,77, 4,24 , 66, 86, 67,5]
juft, toq = split_even_odd(lst)
print(juft)  
print(toq) 

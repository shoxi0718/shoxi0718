import os 
os.system("cls")
ls = [23, 45, 56, 78, 89, 65]
print(ls)
n = int(input("Marhamat Yo'nalishni tanlang \n1: Ko'rish\n2: O'chirish\n3: Sortlash\n4: Toldirish\n"))
match n:
        case 1:
            print("List elementlarini ko'rish")
            print(ls)
        case 2:
            print("List elementlarini o'chirish")
            index = int(input("Nechinchi indeksni o'chirmoqchisiz? "))
            if 0 <= index < len(ls):
                print("Qaysi usul bilan? \n1.pop\n2.clear")
                h = int(input())
                match h:
                    case 1:
                        print("pop() orqali")
                        ls.pop(index) 
                        print(ls)
                    case 2:
                        print("clear() orqali")
                        ls.clear()
                        print(ls)
                    case _:
                        print("Noto'g'ri usul tanlandi.")
            else:
                print("Bu indeksda element mavjud emas.")
        case 3:
            print("List elementlarini sortlash")
            print("sort() orqali")
            ls.sort()  # Kichikdan kattaga qarab tartiblash
            print(ls)

            print("Qaytadan katta dan kichikka sortlash")
            ls.sort(reverse=True)
            print(ls)

            print("Ro'yxatni teskari tartibda")
            ls.reverse()
            print(ls)
        case 4:
            print("List elementlarini sortlash")

            print("Toldirish imkoniyatlari hali qo'shilmagan.")
            print("Noto'g'ri variant tanlandi.")


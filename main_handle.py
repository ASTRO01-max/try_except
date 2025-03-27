# try
# except
# else
# finally

"""ZeroDivisionError"""
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("b soni 0 bo'lib qolgan!, 0 ga bo'lish mumkin emas!")


"""ValueError"""
try:
    a = int(input())

    if a % 2 == 0:
        print("Siz juft son kiritgansiz")
    elif a % 2 != 0:
        print("Siz toq son kiritgansiz")
    else:
        print("Siz manfiy son kiritgansiz")
except ValueError:
    print("Faqat son kiriting!")

"""KeyError"""
try:
    text = input()

    dct = {
        "stol" : "desk",
        "bajarildi" : "done",
        "bugun" : "today",
        "kecha" : "yesterday",
        "kun" : "day"
    }

    print(dct[text])
except KeyError:
    print("Ro'yhatda bunday qiymat yo'q")

"""IndexError"""
try:
    N = int(input())
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst[N])
except:
    print("Siz kiritgan index toplamda mavjud emas!")

"""MemoryError"""
try:
    raise MemoryError  
except MemoryError:
    print("Xatolik: Ro'yxatga siz kiritgan elementlar sig'maydi!")


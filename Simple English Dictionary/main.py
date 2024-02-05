import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #agar foydalanuvchi "Texas" so'zini kiritsa bu "Texas" (ya'ni shtat manosida
        #ham tekshiradi
        return data[w.title()]
    elif w.upper() in data:   # USA yoki  NATO kabi so'zlar kirtilsa
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Bu so'z mavjud emas"
        else:
            return "Biz sining kiritgan so'rovingizni tushuna olmadik"
    else:
        return "Bu so'z mavjud emas emas. Iltimos qayta urinib ko'ring"

word = input("So'zni kiriting: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)






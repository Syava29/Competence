import re 
word = input()
filename = "primer.txt"
ffile = open(filename,'r',encoding="utf-8")

print('Слово "' + word +'" встречается' if word in ffile.read() else 'Нет такого слова')
print(ffile)

with open('primer.txt', encoding="utf-8") as f:
    s = f.read()

search_text = r"информационных"
allres = re.findall(search_text, s)

print(allres)

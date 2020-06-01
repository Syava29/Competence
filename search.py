word = input()
filename = "primer.txt"
ffile = open(filename,'r',encoding="utf-8")
print('Слово "' + word +'" встречается' if word in ffile.read() else 'Нет такого слова')
print(ffile)
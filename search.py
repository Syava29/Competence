word = input()
filename = "primer.txt"
ffile = open(filename,'r',encoding="utf-8")
print('Есть код' if word in ffile.read() else 'Нет кода')
print(ffile)
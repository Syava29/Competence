#import openpyxl as excl
from openpyxl import load_workbook
import numpy as np
import re 

filename1 = "Компетенции.xlsx"
filename2 = "load.txt"
filename3 = "key_word.txt"

spisok = []
spisok_book = []
spisok_description = []

word = input()
komp = input()
filename = "load.txt"
ffile = open(filename,'r')




text_file = open(filename2, 'w')
text_file2 = open(filename3, 'w')

wb = load_workbook(filename1)
sheet = wb.get_sheet_by_name('Лист1')
mtrx = np.zeros([100,3])

sheet.cell(row=1, column=2).value
for row in sheet['A1':'D35']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    text_file.write(string)

wb = load_workbook(filename1)
sheet = wb.get_sheet_by_name('Лист1')

sheet.cell(row=1, column=2).value
for row in sheet['D1':'D35']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    spisok.append(string)
    text_file2.write(string)


#сравниваем ключивые слова и литературу
wb = load_workbook(filename1)
sheet = wb.get_sheet_by_name('Лист1')

sheet.cell(row=1, column=2).value
for row in sheet['E1':'E3']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    spisok_book.append(string)
print(spisok_book)

print('Слово "' + word +'" встречается' if word in ffile.read() else 'Нет такого слова')


text_file.close()

if komp == "УК-1":
    key_word = spisok[0]


with open('load.txt') as f:
    s = f.read()

search_text = spisok[1]
#search_text = r"философии"
allres = re.findall(search_text, s)
if allres !=0: 
    print("OKOKOK")

print(allres)

print(key_word)

#import openpyxl as excl
from openpyxl import load_workbook
import numpy as np
import re 
#название файлов
filename1 = "Компетенции.xlsx"
filename2 = "load.txt"
filename3 = "key_word.txt"
filename4 = "soderzh.txt"
#Листы 
spisok = []
spisok_book = []
spisok_description = []


komp = input()    #     ввод индикатора компетенции пользователем

filename = "load.txt"
ffile = open(filename,'r')

soderzh = open(filename4, 'w')
text_file = open(filename2, 'w')
text_file2 = open(filename3, 'w')
#       считываем данные из excel
wb = load_workbook(filename1)
sheet = wb['Лист1']
mtrx = np.zeros([100,3])

sheet.cell(row=1, column=2).value
for row in sheet['A1':'C35']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    text_file.write(string)
    result_main = re.findall(r'\w+', string)
   

for row in sheet['D1':'D35']:
    string1 = ''
    for cell in row:
        string1 = string1 + str(cell.value)
    spisok.append(string1)

    result_key = re.findall(r'\w+', string1)
    

#сравниваем ключивые слова и литературу

for row in sheet['E1':'E3']:
    string2 = ''
    for cell in row:
        string2 = string2 + str(cell.value) + '\n\n'
    spisok_book.append(string2)
    result1 = re.findall(r'\w+', string2)
    
print('Список литературы : ' + str(spisok_book))


for row in sheet['F1':'F3']:
    string3 = ''
    for cell in row:
        string3 = string3 + str(cell.value) + '\n\n'
    spisok_description.append(string3)
    soderzh.write(string3)
    result1 = re.findall(r'\w+', string3)
    


text_file.close()
with open('load.txt') as f:
    s = f.read()

#предлагаем лиетратуру

if komp == "УК-1":
    
    fword = re.search(r'\w+', str(spisok_description))
    search_text = spisok[00]
    allres = re.findall(search_text, str(spisok_description))
    
    k1 = 0
    if search_text == allres[0]:
        print('К данной компетенции подходит книга : ' + str(fword.group(0)))

#предлагаем лиетратуру
if komp == "УК-2":
   
    fword = re.search(r'\w+', str(spisok_description))
    search_text = spisok[0]
    allres = re.findall(search_text, str(spisok_description))
    
    k1 = 0
    if search_text == allres[0]:
        print('К данной компетенции подходит книга : ' + str(fword.group(0)))
#предлагаем лиетратуру
if komp == "УК-3":
    search_text = spisok[2]
    allres = re.findall(search_text, s)
    if search_text == allres[0]:
        print('К данной компетенции подходит книга : ' + spisok_book[2])
    

search_text = spisok[1]
#search_text = r"философии"
allres = re.findall(search_text, s)
if allres !=0: 
    print("Литература есть")


strstr = open(filename,'r')

result1 = re.findall(r'\w+', string3)





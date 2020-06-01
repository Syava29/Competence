#import openpyxl as excl
from openpyxl import load_workbook
import numpy as np
import re 

filename1 = "Компетенции.xlsx"
filename2 = "load.txt"
filename3 = "key_word.txt"
filename4 = "soderzh.txt"

spisok = []
spisok_book = []
spisok_description = []


komp = input()
filename = "load.txt"
ffile = open(filename,'r')

soderzh = open(filename4, 'w')
text_file = open(filename2, 'w')
text_file2 = open(filename3, 'w')

wb = load_workbook(filename1)
sheet = wb['Лист1']
mtrx = np.zeros([100,3])

sheet.cell(row=1, column=2).value
for row in sheet['A1':'D35']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    text_file.write(string)


for row in sheet['D1':'D35']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    spisok.append(string)
    text_file2.write(string)


#сравниваем ключивые слова и литературу

for row in sheet['E1':'E3']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    spisok_book.append(string)

print('Список литературы : '+str(spisok_book))


for row in sheet['F1':'F3']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
    spisok_description.append(string)
    soderzh.write(string)



text_file.close()
with open('load.txt') as f:
    s = f.read()


if komp == "УК-1":
    search_text = spisok[0]
    allres = re.findall(search_text, s)
    k1 = 0
    if search_text == allres[0]:
        print('К данной компетенции подходит книга : ' + spisok_book[0])
 #for value in enumerate(spisok_book, 1):

  # print('К данной компетенции подходит книга : ' + spisok_book[0])           
     
   
   # if search_text == allres[0]:
      #  print('К данной компетенции подходит книга : ' + spisok_book[0])


if komp == "УК-2":
    search_text = spisok[1]
    allres = re.findall(search_text, s)
    if search_text == allres[0]:
        print('К данной компетенции подходит книга : ' + spisok_book[1])

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





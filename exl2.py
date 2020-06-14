#import openpyxl as excl
from collections import Counter
from openpyxl import load_workbook
import numpy as np
import re 

#название файлов
filename1 = "Компетенции.xlsx"
filename_books = "spisok_knig.xlsx"

filename2 = "load.txt"
filename3 = "key_word.txt"
filename4 = "soderzh.txt"
#Листы 
spisok = []
spisok_book = []
spisok_description = []
spisok_zuv = []
spisok_content = []
#komp = input()    #     ввод индикатора компетенции пользователем

filename = "load.txt"
ffile = open(filename,'r')

soderzh = open(filename4, 'w')
text_file = open(filename2, 'w')
text_file2 = open(filename3, 'w')
#       считываем данные из excel
wb = load_workbook(filename1)
wb_books = load_workbook(filename_books)
sheet_books = wb_books['Лист1']
sheet = wb['Лист1']








# Загружаем ЗУВы и разбиваем их на слова, а также удаляем Знать, Уметь, Владеть
for row in sheet['C1':'C35']:
    zuv = ''
    for cell in row:
        zuv = zuv + str(cell.value)
        your_string = zuv
        removal_list = ['Знать','Уметь','Владеть', ' и ', 'для', 'None', ' в ', ' на ', 'знать']
        for word in removal_list:
            your_string = your_string.replace(word, '')   
        
    result_key = re.findall(r'\w+', your_string)
    col_count = Counter(result_key).most_common(5)    
    
    result_main23 = re.sub(r'\d', '', str(col_count))
    res_res = re.findall(r'\w+', result_main23)
        
     
       
    spisok_zuv.append(result_main23) # Список слов из ЗУВ для каждой компетенции для сравнния с литературой
        
    #print(res_res)

# Парсим Содержание книг
sheet_books.cell(row=2, column=1).value
for row in sheet_books['A1':'CO4']:
    string = ''
    for cell in row:
        string = string + str(cell.value) + '\n\n'
        your_string = string
        removal_list = [' и ',' а ','None' , 'Глава', ' в ']
        for word in removal_list:
            your_string = your_string.replace(word, '')  
    
    result_main = re.sub(r'\d', '', your_string)
    result_main = re.findall(r'\w+', result_main)
    col_count_books = Counter(result_main).most_common(5)
    res_main = re.sub(r'\d', '', str(col_count_books))
    
    testtt = Counter(result_main)
    #print(testtt.keys())
    result111=list(set(spisok_zuv) & set(testtt.keys()))
    
    spisok_content.append(testtt.keys(3))  # Список слов из содержаний книг
   













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
#result111=list(set(spisok_content) & set(result_main))

#print(result111)

#search_text = spisok[1]
#search_text = r"философии"
#allres = re.findall(search_text, s)
#if allres !=0: 
  #  print("Литература есть")

#strstr = open(filename,'r')

#result1 = re.findall(r'\w+', string1)
#result111=list(set(col_count) & set(spisok))

#print(result111)


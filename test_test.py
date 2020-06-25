from collections import Counter





from tkinter import *  
  
  
def clicked():  
    res = "Введите код компетенции (УК-1 ... ПК-23) {}".format(txt.get())  
    lbl.configure(text=res)  
  
  
window = Tk()  
window.title("Подбор литературы по компетенциям")  
window.geometry('400x250')  
lbl = Label(window, text="Введите код компетенции (УК-1 ... ПК-23)")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Подобрать литературу", command=clicked)  
btn.grid(column=2, row=0)  
window.mainloop()



# Создать список

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

col_count = Counter(z)

print(col_count)

  

col = ['blue','red','yellow','green']

  
# Здесь зеленого нет в col_count
# так что счетчик зеленого будет равен нулю

for color in col:

    print (color, col_count[color])


result111=list(set(z) & set(col))
print(result111)

from collections import Counter

d ='aabbbcccdeff'

d = Counter(d)

  
# Для печати значения счетчика

print("d :", d) 

  
# Для доступа к значениям соответствует каждому ключу возвращаемого словаря

print("d.values() : ", d.values())  

  
# Получить ключи и значения как из словаря

print("d.items() :", d.items())

  
# Чтобы получить только ключи

print("d.keys() :", d.keys())

  
# Сортировать значения словаря

print("sorted(d) :", sorted(d))

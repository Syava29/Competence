from collections import Counter
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
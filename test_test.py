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
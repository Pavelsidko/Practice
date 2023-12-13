import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names = np.append(names, 'Pasha')

data3 = np.random.randn(8, 4)

# выбираем строки с нашим именем
my_name = names == 'Pasha'
print("Строки с нашим именем:\n", data3[my_name]) 

# выбираем строки, кроме 'Bob'
not_bob = names != 'Bob'
print("Строки, кроме 'Bob':\n", data3[not_bob])

# выбираем строки только с нашим именем
only_us = (names == 'Alice') | (names == 'Bob')
print("Строки только с нашим именем:\n", data3[only_us])

# выбираем строки 'Bob' или 'Will'
bob_or_will = (names == 'Bob') | (names == 'Will')
print("Строки 'Bob' или 'Will':\n", data3[bob_or_will])

# заменяем отрицательные значения нулями
data3[data3 < 0] = 0
print("Массив data3 после замены отрицательных значений:\n", data3)

# удаляем дубликаты в массиве names с помощью numpy.unique
unique_names = np.unique(names)
print("Массив names после удаления дубликатов с помощью numpy.unique:\n", unique_names)

# удаляем дубликаты в массиве names с помощью set и преобразования обратно в numpy array
unique_names = np.array(list(set(names)))
print("Массив names после удаления дубликатов с помощью set:\n", unique_names)
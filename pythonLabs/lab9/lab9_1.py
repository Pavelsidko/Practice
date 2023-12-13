import numpy as np

# Создание массива
data = np.arange(-20, 181, 3)
print("Количество элементов:", len(data))

# Операции с массивом
print("Умножение на 10:", data * 10)
print("Деление на 5:", data / 5)
print("Сложение:", data + data)
print("Деление на 1/data:", 1 / data)
print("Возведение в квадрат:", data ** 2)
import numpy as np

data3 = np.random.randn(8, 4)

# Сумма, минимум, максимум и среднее значение всех элементов
print("Сумма всех элементов:", np.sum(data3))
print("Минимальное значение:", np.min(data3))
print("Максимальное значение:", np.max(data3))
print("Среднее значение:", np.mean(data3))

# Минимальное, максимальное и средние значения по столбцам
print("Минимальные значения по столбцам:", np.min(data3, axis=0))
print("Максимальные значения по столбцам:", np.max(data3, axis=0))
print("Средние значения по столбцам:", np.mean(data3, axis=0))

# Сумма по строкам
print("Суммы по строкам:", np.sum(data3, axis=1))

# Количество положительных и отрицательных элементов
positive_count = np.sum(data3 > 0)
negative_count = np.sum(data3 < 0)
print("Количество положительных элементов:", positive_count)
print("Количество отрицательных элементов:", negative_count)

# Проверка наличия элемента меньше 0.9
if np.any(data3 < 0.9):
    print("Есть элемент меньше 0.9")
else:
    print("Нет элемента меньше 0.9")

# Проверка всех элементов больше 0.1
if np.all(data3 > 0.1):
    print("Все элементы больше 0.1")
else:
    print("Не все элементы больше 0.1")


# Задание № 6

data4 = np.where(data3 > 0, 2, data3)
print("Массив data4 с заменой положительных значений на 2:\n", data4)

data5 = np.where(data3 < 0, -2, data3)
print("Массив data5 с заменой отрицательных значений на -2:\n", data5)

data6 = np.where(data3 > 0, 2, np.where(data3 < 0, -2, data3))
print("Массив data6 с заменой положительных значений на 2 и отрицательных на -2:\n", data6)

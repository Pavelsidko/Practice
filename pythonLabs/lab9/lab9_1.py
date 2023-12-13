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

# Основные математические функции библиотеки NumPy
print("Абсолютное значение:", np.abs(data))
print("Квадратный корень:", np.sqrt(data))
print("Квадрат элементов:", np.square(data))
print("Экспонента:", np.exp(data))
print("Натуральный логарифм:", np.log(data))
print("Двоичный логарифм:", np.log2(data))
print("Десятичный логарифм:", np.log10(data))
print("Градусы:", np.degrees(data))
print("Радианы:", np.radians(data))
print("Синус:", np.sin(data))
print("Косинус:", np.cos(data))
print("Тангенс:", np.tan(data))
print("Арккосинус:", np.arccos(data))
print("Арксинус:", np.arcsin(data))
print("Арктангенс:", np.arctan(data))




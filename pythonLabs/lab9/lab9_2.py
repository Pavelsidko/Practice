import numpy as np

# Создание массивов
arr1 = np.array([[9, 2, 7], [1, 4, 3]])
arr2 = np.array([[8, 2, 5], [3, 4, 1]])


print("arr1 > arr2:\n", arr1 > arr2)
print("arr1 < arr2:\n", arr1 < arr2)
print("arr1 == arr2:\n", arr1 == arr2)
print("arr1 != arr2:\n", arr1 != arr2)
print("arr1 >= arr2:\n", arr1 >= arr2)
print("arr1 <= arr2:\n", arr1 <= arr2)

# добавление новой строки
new_row = np.array([5, 6, 7])
arr1 = np.insert(arr1, 1, new_row, axis=0)

print("Массив arr1 с добавленной строкой:\n", arr1)

# добавление нового столбца
new_col = np.array([5, 6, 7])
arr1 = np.insert(arr1, 1, new_col, axis=1)

print("Массив arr1 с добавленным столбцом:\n", arr1)

# добавление новой строки
new_row = np.array([5, 6, 7])
arr2 = np.append(arr2, [new_row], axis=0)

print("Массив arr2 с добавленной строкой:\n", arr2)

# добавление нового столбца
new_col = np.array([5, 6, 7])
arr2 = np.insert(arr2, arr2.shape[1], new_col, axis=1)

print("Массив arr2 с добавленным столбцом:\n", arr2)


result = arr1[0,0] + arr1[-1,0] + arr1[0,-1] + arr1[-1,-1]
print("Результат суммы:", result)

result = arr1[0,0] * arr1[-1,0] * arr1[0,-1] * arr1[-1,-1]
print("Результат произведения:", result)



# первые две строки
sliced1 = arr2[:2,:]
print("Первые две строки:\n", sliced1)

# последние два столбца
sliced2 = arr2[:, -2:]
print("Последние два столбца:\n", sliced2)

# первые два столбца из второй строки
sliced3 = arr2[1, :2]
print("Первые два столбца из второй строки:", sliced3)

# последние две строки из третьего столбца
sliced4 = arr2[-2:, 2]
print("Последние две строки из третьего столбца:\n", sliced4)




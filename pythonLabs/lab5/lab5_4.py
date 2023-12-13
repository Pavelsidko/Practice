n = int(input()) # размер массива
arr = list(map(int, input().split())) # элементы массива
k, m = map(int, input().split()) # начальный и конечный индексы части массива
r = int(input()) # величина сдвига

# циклический сдвиг
shifted_part = arr[k-1:m]
shifted_part = shifted_part[r:] + shifted_part[:r]

# замена части массива на сдвинутую часть
arr[k-1:m] = shifted_part

# вывод результата
print(*arr)
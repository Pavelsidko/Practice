import numpy as np

arr = np.empty((7, 6))

for i in range(arr.shape[0]):
    arr[i] = i
print("Исходный массив: \n", arr)

sub_arr = arr[[2, 1, 0, 5]]
print("Исходный массив-подмножество:\n", sub_arr)

transposed_sub_arr = sub_arr.T
print("Транспонированный массив-подмножество:\n", transposed_sub_arr)

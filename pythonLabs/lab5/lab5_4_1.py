def cyclic_shift(N, array, K, M, R):
   # Create a new array with the cyclic shift
   new_array = array[:K-1] + array[K-1:M] + array[M-1:M-R+1] + array[M-R:K-1] + array[K-1:M]
   return new_array

# Input data
n = int(input()) # размер массива
arr = list(map(int, input().split())) # элементы массива
k, m = map(int, input().split()) # начальный и конечный индексы части массива
r = int(input()) # величина сдвига

# Perform the cyclic shift
result = cyclic_shift(n, arr, k, m, r)

# Print the result
for i in result:
   print(i, end=' ')
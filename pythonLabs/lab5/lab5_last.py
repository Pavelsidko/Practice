



n = int(input()) # размер массива
arr = list(map(int, input().split())) # элементы массива
k, m = map(int, input().split()) # начальный и конечный индексы части массива
r = int(input()) # величина сдвига

k-=1
m-=1

arr2 = arr[k:m+1]
for _ in range(r):
    arr2 = arr2[1:n] + [arr2[0]]

print(*(arr[:k] + arr2 + arr[m + 1:]))

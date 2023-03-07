def binarySearch(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif arr[mid] < x:  # искомый элемент меньше центрального
                        # значит следует искать в левой половине
        # print(f'left:{left}')
        print(f'mid:{mid}')
        return binarySearch(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
arr.reverse()
x = 7
# изначально мы запускаем двоичный поиск на всей длине массива
print(arr)
index = binarySearch(arr, x, left=0, right=len(arr))
print(index)

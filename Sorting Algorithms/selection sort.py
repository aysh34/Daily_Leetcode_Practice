def selectionSort(arr):
    for i in range(len(arr)):  # i points to the index of first element of unsorted portion
        min_idx = i

        # after 1st pass the minimum element will be at 0 index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap minimum element with first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(arr))

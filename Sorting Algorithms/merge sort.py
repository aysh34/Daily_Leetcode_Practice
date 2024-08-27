def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]

    left_sort = mergeSort(left)
    right_sort = mergeSort(right)

    return merge(left_sort, right_sort)


def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(mergeSort([5,3,8,4,2,7,6,1]))
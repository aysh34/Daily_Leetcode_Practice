def bubbleSort(arr):
    swap = False
    for i in range(len(arr)):
        # each step, the largest element will be at the end
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        
        if not swap:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))    
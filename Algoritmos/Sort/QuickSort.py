def partition(arr, start, end):
    p = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort(arr, start, end):
    if start< end:
        pivot = partition(arr, start , end)
        #left
        quickSort(arr, start ,pivot -1 )
        #right
        quickSort(arr, pivot + 1 ,end)
    return arr 

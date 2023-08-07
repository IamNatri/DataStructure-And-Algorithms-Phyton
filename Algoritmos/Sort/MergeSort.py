def mergeSort(arr):
    #div arr until 
    if len(arr) > 1:
        div = len(arr) // 2
        left = arr[:div].copy()
        rigth = arr[div:].copy()

        mergeSort(left)
        mergeSort(rigth)

        i = j = k = 0

        #ord left rigth

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                arr[k] = left[i]

                i+=1
            else:
                arr[k] = rigth[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k += 1
        while j < len(rigth):
            arr[k] = rigth[j]
            i+=1
            k += 1

        return arr


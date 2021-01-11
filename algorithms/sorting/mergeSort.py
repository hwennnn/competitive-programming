arr = [1,-1,5,9,0,100,45]

def mergeSort(arr, start, end):
    if start >= end: return
    
    mid = (start+end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)

    merge(arr,start, mid, end)

def merge(arr, start, mid, end):
    res = [None] * len(arr)
    
    left_start = start
    left_end = mid
    right_start = mid+1
    right_end = end
    
    k = start
    while left_start <= left_end and right_start <= right_end:
        if arr[left_start] < arr[right_start]:
            res[k] = arr[left_start]
            left_start += 1
        else:
            res[k] = arr[right_start]
            right_start += 1
        
        k += 1
    
    while left_start <= left_end:
        res[k] = arr[left_start]
        left_start += 1
        k += 1
    
    while right_start <= right_end:
        res[k] = arr[right_start]
        right_start += 1
        k += 1

    for x in range(start, end+1):
        arr[x] = res[x]
    
mergeSort(arr, 0, len(arr)-1)

print(arr)
    
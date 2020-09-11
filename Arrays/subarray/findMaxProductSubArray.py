# find maximum product subarray

arr = [1, -3, -5, -2, 0, 4]

pos = arr[0]
neg = arr[0]
res = arr[0]
print(pos, neg, res)
for i in range(1, len(arr)):
    
    if arr[i] > 0:
        pos = max(pos*arr[i], arr[i])
        neg = min(neg*arr[i], arr[i])
    
    else:
        tempMax = max(neg*arr[i], arr[i])
        neg = min(pos*arr[i], arr[i])
        pos = tempMax
    
    
    res = max(res, pos)
    print(pos, neg, res)
print(res)
# find maximum product subarray

arr = [5,-2,-1,-5,0,100]

pos = 1
neg = 1
res = 1

for i in range(len(arr)):
    if arr[i] > 0:
        pos *= arr[i]
        neg = min(1, neg*arr[i])
    
    elif arr[i] == 0:
        pos = 1
        neg = 1
    
    else:
        temp = pos
        pos = max(neg * arr[i],1)
        neg = temp * arr[i]
    
    res = max(res, pos)

print(res)
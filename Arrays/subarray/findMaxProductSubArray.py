# find maximum product subarray

def solve(arr):
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
    return res

print(solve([2,3,-2,4,-10]))
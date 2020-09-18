n, target = map(int,input().split())
arr = list(map(int,input().split()))

def solve(n, target, arr):
    
    arr = sorted({num:i+1 for i,num in enumerate(arr)}.items())
    print(arr)
    for i in range(n-2):
        a = arr[i][0]
        l, r = i+1, n-1
        
        while l < r:
            print(i,l,r)
            s = arr[i][0] + arr[l][0] + arr[r][0]
            
            if s == target:
                print(arr[i][1],arr[l][1],arr[r][1])
                return 0
            
            elif s > target:
                r -= 1
            
            else:
                l += 1
    
    print("IMPOSSIBLE")
        
solve(n, target, arr)
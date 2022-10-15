def solution():
    n = int(input())
    arr = [int(i) for i in input().split()]

    s = set()
    j = 0
    count = 0

    for i in range(n):
        
        while arr[i] in s:
            s.remove(arr[j])
            j += 1
            
        s.add(arr[i])
        count = max(count, len(s))
       

    print(count)
    
if __name__ == "__main__":
    solution()
    

        
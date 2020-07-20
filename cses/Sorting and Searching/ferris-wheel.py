def solution():
        
# 2 3 7 9
 
    line1 = list(map(int, input().split()))
    n, m = line1[0], line1[1]
    
    weights = list(map(int, input().split()))
    
    weights.sort()
    i, j, total = 0, n-1, 0
    curr = weights[j]
    taken = 1
    
    while (i<j):
        if taken == 2:
            total += 1
            j -= 1
            taken = 1
            curr = weights[j]
            
 
        elif weights[i] + curr > m:
            total += 1
            taken = 1
            j -= 1
            curr = weights[j]
        
        else:
            taken += 1
            i += 1
        
    
    print(total + 1)
 
          
if __name__ == "__main__":
    solution()
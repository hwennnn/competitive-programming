def solution():
        
    line1 = list(map(int,input().split()))
    n, m, k = line1[0], line1[1], line1[2]
    
    peeps = list(map(int,input().split()))
    apps = list(map(int,input().split()))
    
    peeps.sort()
    apps.sort()
    
    ans = i = j = 0
    
    # Applicant: 45 60 60 80
    # Apartment: 30 60 75
    
    while i < n and j < m:
        
        if abs(peeps[i]-apps[j]) <= k:
            ans += 1
            i += 1
            j += 1
        
        elif peeps[i] > apps[j]:
            j += 1
        
        else:
            i += 1
    
    print(ans)
    
if __name__ == "__main__":
    solution()
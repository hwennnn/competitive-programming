N = int(input())

asc = []
desc = []

for _ in range(N):
    tmp = [int(i) for i in input().split()]

    if tmp[0] <= tmp[1]:
        asc.append(tmp)
    else:
        desc.append(tmp)

asc = sorted(asc, key = lambda x : (x[0], x[1]))
desc = sorted(desc, key = lambda x : (-x[0], -x[1]))

a = 1 if asc else 0
a_curr = asc[0]
a_res = []
a_res.append(a_curr)

for x1,x2 in asc[1:]:
    c1 = a_curr[0]
    c2 = a_curr[1]

    if x2 >= c2:
        a_curr[1] = max(c2, x2)
    
    else:
        a_curr = [x1,x2]
        a_res.append(a_curr)
        a += 1
    
d = 1 if desc else 0
d_curr = desc[0]
d_res = []
d_res.append(d_curr)


for x1, x2 in desc[1:]:
    c1 = d_curr[0]
    c2 = d_curr[1]
    
    if x2 <= c2:
        d_curr[1] = min(x2, c2)
    
    else:
        d_curr = [x1,x2]
        d_res.append(d_curr)
        d += 1

print(a, a_curr)
print(d, d_curr)
print(a+d)

# Test case 1

# 4 
# 1 2
# 2 3
# 3 1
# 3 4

# => 2

# Test case 2

# 7
# 1 2
# 2 3
# 3 1
# 4 2
# 4 3
# 3 5
# 2 5

# => 2
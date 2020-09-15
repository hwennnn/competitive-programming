# NOTE: You can use the following values to test this function.
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 24
# closest_sum_pair(a1, a2, a_target) should return (5, 20) or (3, 20).

b1 = [7, 4, 1, 10]
b2 = [4, 5, 8, 7]
b_target = 13
# closest_sum_pair(b1, b2, b_target) should return (4,8), (7, 7), (7, 5), or (10, 4).

c1 = [6, 8, -1, -8, -3]
c2 = [4, -6, 2, 9, -3]
c_target = 3
# closest_sum_pair(c1, c2, c_target) should return (-1, 4) or (6, -3).

d1 = [19, 14, 6, 11, -16, 14, -16, -9, 16, 13]
d2 = [13, 9, -15, -2, -18, 16, 17, 2, -11, -7]
d_target = -15
# closest_sum_pair(d1, d2, d_target) should return (-16, 2) or (-9, -7).

def closest_sum_pair(A, B, target):
    A = sorted(A)
    B = sorted(B)
    
    min_diff = abs(A[0] + B[0] - target)
    min_pair = (A[0], B[0])
    
    i = 0
    j = len(A)-1
    
    while i < len(A) and j > 0:
        v1 = A[i]
        v2 = B[j]
        diff = v1 + v2 - target
        
        if abs(diff) < min_diff:
            min_diff = abs(diff)
            min_pair = (v1, v2)
        
        if diff == 0:
            return min_pair
        
        elif diff < 0:
            i += 1
        
        else:
            j -= 1
    
    return min_pair


print(closest_sum_pair(a1,a2,a_target))
print(closest_sum_pair(b1, b2, b_target))
print(closest_sum_pair(c1, c2, c_target))
print(closest_sum_pair(d1, d2, d_target))
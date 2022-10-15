n = int(input())

lines = []
maxN = float('-inf')

for i in range(n):
    width, height = map(int, input().split())
    lines.append((i, i + width, height))
    maxN = max(maxN, i + width)

A = [0] * (maxN + 1)

for start, end, height in lines:
    A[start] += height
    A[end] -= height

res = float('-inf')
for i in range(1, len(A)):
    A[i] += A[i - 1]
    res = max(res, A[i])

print(res)

'''
Test case 1

5
2 3
2 1
1 2
3 2
1 3

=> 5
'''

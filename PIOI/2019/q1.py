row, col = map(int, input().split())

arr = [[0]*col for _ in range(row)]

for i in range(row):
    tmp = [int(i) for i in input().split()]
    for j in range(col):
        arr[i][j] = tmp[j]

res = 0
for i in range(1, row):

    for j in range(col):
        if arr[i][j]:
            a = 0 if j - 1 < 0 or not arr[i-1][j-1] else arr[i-1][j-1]
            b = 0 if not arr[i-1][j] else arr[i-1][j]
            c = 0 if j + 1 >= col or not arr[i-1][j+1] else arr[i-1][j+1]

            m = max(a, b, c)
            if m:
                arr[i][j] = m + arr[i][j]
            else:
                arr[i][j] = 0

        if i + 1 == row:
            res = max(res, arr[i][j])

print(res-row)

'''
Test case 1

6 5
1 3 8 10 0
3 0 1 5 0
6 5 9 1 4
9 7 2 6 4
4 8 7 3 10
10 10 3 1 8

=> 43

Test case 2

5 5
0 0 1 0 0
0 0 1 1 9
0 9 9 1 0
0 9 0 0 1
0 0 0 1 0

=> 0
'''

import bisect


def solve():
    n = int(input())
    A = [int(x) for x in input().split()]
    res = []

    for x in A:
        index = bisect.bisect_left(res, x)
        if index < len(res):
            res[index] = x
        else:
            res.append(x)

    print(len(res))


solve()

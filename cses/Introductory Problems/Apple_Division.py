#!/usr/bin/env python3
import sys
import math
import random
import functools
import itertools
import collections
import heapq
import bisect
from collections import Counter, defaultdict, deque

M = 10**9 + 7
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
MININT = -MAXINT - 1


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x-1 for x in arr]


def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve():
    n = int(input())
    A = [int(x) for x in input().split()]
    total = sum(A)
    res = 0

    for mask in range(1 << n):
        curr = 0

        for j in range(n):
            if (1 << j) & mask:
                curr += A[j]

        if curr <= total // 2:
            res = max(res, curr)

    print(total - res - res)


if __name__ == "__main__":
    solve()

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
input = sys.stdin.readline  # to read input quickly

M = 10**9 + 7  # 998244353
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
    N = int(input())

    if N == 1:
        return "1"
    elif N < 4:
        return "NO SOLUTION"
    elif N == 4:
        return "3 1 4 2"
    else:
        res = []

        for x in range(1, N + 1, 2):
            res.append(x)

        for x in range(2, N + 1, 2):
            res.append(x)

        return " ".join(map(str, res))


print(solve())

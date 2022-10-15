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
    for _ in range(int(input())):
        k = int(input())

        length = first = 1
        while k > 9 * first * length:
            k -= 9 * first * length
            length += 1
            first *= 10

        q, r = divmod(k-1, length)
        print(str(first + q)[r])


if __name__ == "__main__":
    solve()

#!/usr/bin/env python3
from io import BytesIO, IOBase
import os
import sys
import math
import random
import functools
import itertools
import collections
from heapq import heappush, heappop, heappushpop, heapify
import bisect
from collections import Counter, defaultdict, deque


# region fastio

BUFSIZE: int = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")

# endregion


M = 10**9 + 7
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
MININT = -MAXINT - 1


class Solution():
    def solve(self):
        N, M = map(int, input().split())

        A = [int(x) for x in input().split()]

        graph = defaultdict(list)

        for _ in range(M):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append((v, w))
            graph[v].append((u, w))

        weights = [float('inf')] * N
        weights[0] = 0

        parents = defaultdict(list)

        # src, weight, paths
        pq = [(0, 0, [-1] * N)]

        while pq:
            weight, src, prev = heappop(pq)
            prev = prev[:]
            if weights[src] != weight:
                continue

            for nei, w in graph[src]:
                old = weights[nei]
                new = weight + w

                if new < old:
                    weights[nei] = new
                    prev[nei] = src
                    parents[nei].append(prev)
                    heappush(pq, (new, nei, prev))
                elif new == old:
                    prev[nei] = src
                    parents[nei].append(prev)
                    heappush(pq, (new, nei, prev))

        def median():
            nonlocal N

            res = float('-inf')

            for parent in parents[N - 1]:
                paths = [A[-1]]
                x = parent[-1]

                while x != -1:
                    paths.append(A[x])
                    x = parent[x]

                paths.sort()
                n = len(paths)

                if len(paths) & 1:
                    res = max(res, paths[n // 2])
                else:
                    res = max(res, (paths[n // 2] + paths[(n // 2) - 1]) // 2)

            return res

        print(f"{weights[-1]} {median()}")


if __name__ == "__main__":
    solution = Solution()
    solution.solve()

'''
8 10
1 1 1 1 2 2 2 2
1 2 1
1 3 1
2 4 1
4 3 1
4 5 1
4 7 1
8 5 1
8 7 1
6 2 1
6 7 1
'''

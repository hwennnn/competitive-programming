# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for mat in matrix:
            for m in mat:
                if len(heap) == k:
                    heapq.heappushpop(heap, -m)
                else:
                    heapq.heappush(heap, -m)
​
        return -heap[0]

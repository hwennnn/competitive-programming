# 1887. Reduction Operations to Make the Array Elements Equal
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mmin = min(nums)
        heap = []
        counter = collections.Counter(nums)
        for num,count in counter.items():
            if num != mmin:
                heap.append((-num, count))
        
        heapq.heapify(heap)
        
        res = 0
        while len(heap) > 0:
            num, count = heapq.heappop(heap)
            num = -num
            res += count
            
            if heap:
                nextNum, nextCount = heapq.heappop(heap)
                heapq.heappush(heap, (nextNum, nextCount + count))
        
        return res
        
            

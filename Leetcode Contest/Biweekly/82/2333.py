# 2333. Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        pq = []
        
        for a, b in zip(nums1, nums2):
            heappush(pq, ((-abs(a - b), 1)))
        
        orders = k1 + k2
        
        while pq and orders > 0:
            flag = True
            top, count = heappop(pq)
            top = -top
            
            while pq and top == -pq[0][0]:
                count += heappop(pq)[1]
            nextTop = 0
            if pq:
                nextTop = -pq[0][0]
                
            delta = top - nextTop
            if delta * count <= orders:
                orders -= (delta * count)
            else:
                flag = False
                heappush(pq, (-top, count))
                
                while pq and orders > 0:
                    x, cnt = heappop(pq)
                    take = min(orders, cnt)
                    orders -= take
                    heappush(pq, (x + 1, take))
                    if cnt != take:
                        heappush(pq, (x, cnt - take))
​
            if flag and nextTop:
                heappush(pq, (-nextTop, count))
​
        total = 0
        for x, count in pq:
            total += x * x * count
            
        return total 
                
                
            
            

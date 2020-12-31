# 1482. Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if n < m*k: return -1
        
        def good(day):
            flowers = [i for i,x in enumerate(bloomDay) if x <= day]
            
            nf = len(flowers)
            count = i = 0
            
            while i < nf-k+1:
                if (flowers[i+k-1] - flowers[i]) == k-1:
                    count += 1
                    i += k
                else:
                    i += 1
                    
            return count >= m
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left+right)//2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
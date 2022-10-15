# 2053. Kth Distinct String in an Array
# https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)
        
        for x, v in counter.items():
            if v == 1:
                k -= 1
                
                if k == 0: return x
        
        return "" 

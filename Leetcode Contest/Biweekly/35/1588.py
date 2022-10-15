# 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = sum(arr)
        
        odd = 3
        
        while odd <= n:
            
            for i in range(n-odd+1):
                res += sum(arr[i:i+odd])
            
            odd += 2
        
        return res
            
            
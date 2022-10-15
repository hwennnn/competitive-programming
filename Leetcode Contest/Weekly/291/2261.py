# 2261. K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s = set()
        i = 0
        count = 0
        n = len(nums)
        
        def go(arr, start, end): 
            sub_list = [] 
            
            for i in range(start, end + 1): 
                for j in range(i + 1, end + 1): 
                    sub = arr[i:j] 
                    sub_list.append(sub) 
​
            return sub_list
    
        for j, x in enumerate(nums):
            if x % p == 0:
                count += 1
            
            while count > k:
                if nums[i] % p == 0:
                    count -= 1
                i += 1
            
            
            if j == n - 1 or count == k:
                for sub in go(nums, i, j + 1):
                    s.add(tuple(sub))
​
        return len(s)

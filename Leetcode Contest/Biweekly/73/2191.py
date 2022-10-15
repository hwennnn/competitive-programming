# 2191. Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        
        for i, num in enumerate(nums):
            x = str(num)
            curr = ""
            
            for char in x:
                curr += str(mapping[int(char)])
            
            res.append((int(curr), i, num))
            
        res.sort()
        return [num for _, __, num in res]

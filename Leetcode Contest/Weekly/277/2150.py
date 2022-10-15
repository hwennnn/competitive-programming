# 2150. Find All Lonely Numbers in the Array
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        
        for x in counter.keys():
            if counter[x] == 1 and x - 1 not in counter and x + 1 not in counter:
                res.append(x)
        
        return res

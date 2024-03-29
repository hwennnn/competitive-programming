# 982. Triples with Bitwise AND Equal To Zero
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        mp = collections.defaultdict(int)
        res = 0
        
        for a in nums:
            for b in nums:
                mp[a & b] += 1
        
        for c in nums:
            for ab in mp:
                if ab & c == 0:
                    res += mp[ab]
        
        return res

# 2433. Find The Original Array of Prefix Xor
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        res = [pref[0]]
        roll = res[-1]
​
        for i in range(1, N):
            res.append(roll ^ pref[i])
            roll ^= res[-1]
                
        return res

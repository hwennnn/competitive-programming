# 2186. Minimum Number of Steps to Make Two Strings Anagram II
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        
        for x in s:
            if count2[x] > 0:
                count2[x] -= 1
        
        for x in t:
            if count1[x] > 0:
                count1[x] -= 1
        
        return sum(count1.values()) + sum(count2.values())

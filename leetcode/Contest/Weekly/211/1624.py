# 1624. Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, S: str) -> int:
        
        d = collections.defaultdict(list)
        
        for i, s in enumerate(S):
            d[s].append(i)

        return max(d[i][-1] - d[i][0] - 1 for i in d)
    
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        n = len(s)
        res = -1
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    res = max(res, j-i - 1)

        return res 
    
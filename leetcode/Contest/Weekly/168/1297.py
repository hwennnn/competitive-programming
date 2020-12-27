# 1297. Maximum Number of Occurrences of a Substring
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution:
    def maxFreq(self, s: str, maxLetters: int, k: int, maxSize: int) -> int:
        count = collections.Counter()
        
        for i in range(len(s) - k + 1):
            count[s[i:i+k]] += 1
        
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
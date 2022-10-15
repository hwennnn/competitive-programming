# 2416. Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        res = [0] * N
        mp = defaultdict(int)
        
        for word in words:
            prefix = ""
            
            for char in word:
                prefix += char
                mp[prefix] += 1
        
        for index, word in enumerate(words):
            prefix = ""
            count = 0
            
            for char in word:
                prefix += char
                count += mp[prefix]
            
            res[index] = count
        
        return res

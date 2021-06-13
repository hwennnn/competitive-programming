# 1897. Redistribute Characters to Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        mp = collections.defaultdict(int)
        
        for word in words:
            for c in word:
                mp[c] += 1
        
        for key in mp:
            if not (mp[key] >= n and mp[key] % n == 0): return False
        
        return True

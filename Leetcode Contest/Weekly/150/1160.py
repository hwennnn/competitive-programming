# 1160. Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        n = len(words)
        c2 = Counter(chars)
        
        for i in range(n):
            c1 = Counter(words[i])
            if all((c2[c] - c1[c] >= 0) for c in c1):
                res += len(words[i])
        
        
        return res

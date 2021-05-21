# 890. Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def construct(word):
            ptr = 0
            mp = {}
            s = ""
            
            for w in word:
                if w not in mp:
                    mp[w] = ptr
                    ptr += 1
                
                s += str(mp[w])     
                    
            return s
        
        res = []
        p = construct(pattern)
​
        for word in words:
            if construct(word) == p:
                res.append(word)
        
        return res

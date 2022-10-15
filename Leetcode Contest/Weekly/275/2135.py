# 2135. Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        targets = Counter()
        
        def construct(words):
            mask = 0
            for x in words:
                mask |= (1 << ord(x) - ord('a'))
                
            return mask
        
        for words in targetWords:
            mask = construct(words)
            targets[mask] += 1
        
        res = 0
        
        for words in startWords:
            currMask = construct(words)
            
            for i in range(26):
                if currMask & (1 << i) > 0: continue
                
                newMask = currMask | (1 << i)
​
                if newMask in targets:
                    res += targets[newMask]
                    del targets[newMask]
        
        return res
                        
            

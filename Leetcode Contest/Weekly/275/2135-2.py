# 2135. Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        targets = Counter("".join(sorted(words)) for words in targetWords)
        maxLen = len(max(targets.keys(), key = len))
        res = 0
        
        for word in startWords:
            sp = set(word)
            
            for x in string.ascii_lowercase:
                if x in sp: continue
                g = "".join(sorted(word + x))
                if g in targets:
                    targets[g] = 0
        
        return len(targetWords) - sum(targets.values())

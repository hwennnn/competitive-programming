# 2085. Count Common Words With One Occurrence
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s1 = Counter(words1)
        s2 = Counter(words2)
        res = 0
        
        for k, v in s1.items():
            if v == 1 and s2[k] == 1:
                res += 1
        
        return res

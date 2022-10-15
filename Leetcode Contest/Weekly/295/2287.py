# 2287. Rearrange Characters to Make Target String
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        tt = Counter(target)
        
        return min(counter[t] // tt[t] for t in tt)
        
